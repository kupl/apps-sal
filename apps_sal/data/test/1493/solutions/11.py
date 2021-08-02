n, m = list(map(int, input().split()))
BOARD = []
A = ['B', 'W']
for i in range(n):
    BOARD = BOARD + [list(input())]
for i in range(n):
    for j in range(m):
        if BOARD[i][j] == '.':
            BOARD[i][j] = A[(i + j) % 2]
for i in range(n):
    print(''.join(BOARD[i]))
