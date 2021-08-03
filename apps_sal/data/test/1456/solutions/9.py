from sys import stdin

n = int(stdin.readline())

board = []

for x in range(n):
    board.append(list(stdin.readline().strip()))

moves = {y: {x: True for x in range(-n + 1, n)} for y in range(-n + 1, n)}

for x in range(n):
    for y in range(n):
        if board[x][y] == 'o':
            for a in range(n):
                for b in range(n):
                    if board[a][b] == '.':
                        moves[a - x][b - y] = False

recreate = [['.' for x in range(n)] for y in range(n)]

for x in range(n):
    for y in range(n):
        if board[x][y] == 'o':
            recreate[x][y] = 'o'
            for a in moves:
                for b in moves:
                    if moves[a][b]:
                        if 0 <= x + a < n and 0 <= y + b < n:
                            if recreate[x + a][y + b] != 'o':
                                recreate[x + a][y + b] = 'x'

if board == recreate:
    print('YES')

    for x in range(-n + 1, n):
        l = []
        for y in range(-n + 1, n):
            if moves[x][y]:
                l.append('x')
            else:
                l.append('.')
        if x == 0:
            l[n - 1] = 'o'
        print(''.join(l))
else:
    print('NO')
