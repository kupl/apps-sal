from itertools import permutations

n = int(input())

boards = []
for i in range(4):
    board = [input() for j in range(n)]
    boards.append(board)
    if i != 3:
        input()

perms = list(permutations(list(range(4))))


def cost(board):

    base1 = [1, 0] * (len(board) // 2)
    base2 = [0, 1] * (len(board) // 2)

    board1 = []
    board2 = []
    for i in range(len(board) // 2):
        board1.append(base1)
        board1.append(base2)

        board2.append(base2)
        board2.append(base1)

    board = [list(map(int, list(a))) for a in board]

    curr_min_cost1 = 0
    curr_min_cost2 = 0
    for i in range(len(board)):
        for j in range(len(board)):
            curr_min_cost1 += board[i][j] ^ board1[i][j]
            curr_min_cost2 += board[i][j] ^ board2[i][j]

    return min(curr_min_cost1, curr_min_cost2)


min_cost = float('inf')
for p in perms:
    b1 = boards[p[0]] + boards[p[1]]
    b2 = boards[p[2]] + boards[p[3]]
    b = [a + b for a, b in zip(b1, b2)]
    min_cost = min(min_cost, cost(b))

print(min_cost)
