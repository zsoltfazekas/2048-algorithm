import requests
import json
import numpy as np
from game import Game

API = 'https://thegame-2048.herokuapp.com/'

PLAY_THE_GAME = 'api/play_the_game'
NEW_GAME = 'api/new_game'

# r = requests.post(url = API+NEW_GAME, json = {'team_name':'fw'})
# board_status = requests.post(url = API+PLAY_THE_GAME, json={"uId": r.json()['uId'], "direction": "s"})
# game_over = board_status.json()['game_over']



SUM_MAT = [[2**15, 2**14 , 2**13, 2**12], [2**8, 2**9, 2**10, 2**11], [2**7, 2**6, 2**5, 2**4], [2**0, 2**1, 2**2, 2**3]]

# SUM_MAT = [[],[],[],[]]

def heuristic(board):
    summa = 0
    for i in range(4):
        for j in range(4):
            summa = summa + SUM_MAT[i][j]*board[i][j]
    return summa

# def heuristic2(board):
# 	for i in range(4):
# 		for j in range(4):
			

runtime = 0
max_score = 0


# def terminal_node(board_status):
# 	return board_status.json()['game_over']

# def child_board(board_status):
#     child_nodes = []

#     current_game = Game(board_status.json()['board'], 0)
#     move_left  = current_game.process_move('a')
#     if move_left:
#         child_nodes.append(current_game.x)

#     current_game = Game(board_status.json()['board'], 0)
#     move_right  = current_game.process_move('a')
#     if move_left:
#         child_nodes.append(current_game.x)


# def minimax(board, depth, maximizingPlayer):
# 	if (depth == 0) or terminal_node(board):
# 		return heuristic(board)
# 	if maximizingPlayer:
# 		value = np.NINF
# 		for child_board in child_board(board)

while True:
    
    runtime = runtime + 1
    r = requests.post(url = API+NEW_GAME, json = {'team_name':'fw_alg_2'})
    board_status = requests.post(url = API+PLAY_THE_GAME, json={"uId": r.json()['uId'], "direction": "s"})

    game_over = board_status.json()['game_over']

    def move(direction):
        return requests.post(url = API+PLAY_THE_GAME, json={"uId": r.json()['uId'], "direction": direction})
    
    board_status = move('w')
   
    while game_over == False:

	    move_dict = {}
	    
	    current_game = Game(board_status.json()['board'], 0)
	    move_left  = current_game.process_move('a')
	    if move_left:
	        move_dict[heuristic(current_game.x)] = 'a'

	    current_game = Game(board_status.json()['board'], 0)
	    move_right  = current_game.process_move('d')
	    if move_right:
	        move_dict[heuristic(current_game.x)] = 'd'

	    current_game = Game(board_status.json()['board'], 0)
	    move_up  = current_game.process_move('w')
	    if move_up:
	        move_dict[heuristic(current_game.x)] = 'w'

	    current_game = Game(board_status.json()['board'], 0)
	    move_down  = current_game.process_move('s')
	    if move_down:
	        move_dict[heuristic(current_game.x)] = 's'
	    
	    if move_dict == {}:
	    	break

	    step = move_dict.get(max(move_dict, key=int))

	    board_status = move(step)
	    if max_score < board_status.json()['c_score']:
	    	max_score = board_status.json()['c_score']

	    game_over = board_status.json()['game_over']

    print("Number of run: ", runtime)
    print("Maxscore", max_score)