def isConnected(r1, c1, r2, c2, board):
    visited = [[0] * c for i in range(r)]
    Q = [[r1, c1]]
    visited[r1][c1] = 1
    while Q:
        q = Q.pop(0)
        (x, y) = (q[0], q[1])
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < r and 0 <= new_y < c and (visited[new_x][new_y] == 0) and (board[new_x][new_y] == '.'):
                visited[new_x][new_y] = 1
                Q.append([new_x, new_y])
                if new_x == r2 and new_y == c2:
                    return True
    return False


dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
(r, c) = list(map(int, input().split()))
board = [list(input()) for i in range(r)]
(r1, c1) = list(map(int, input().split()))
(r2, c2) = list(map(int, input().split()))
r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1
isX = board[r2][c2] == 'X'
G = []
for i in range(4):
    x = r2 + dx[i]
    y = c2 + dy[i]
    if x >= 0 and x < r and (y >= 0) and (y < c) and (board[x][y] == '.'):
        G.append([x, y])
if abs(r1 - r2) + abs(c1 - c2) == 1:
    if board[r2][c2] == 'X':
        print('YES')
    elif len(G) > 0:
        print('YES')
    else:
        print('NO')
elif r1 == r2 and c1 == c2:
    if len(G) == 0:
        print('NO')
    else:
        print('YES')
elif len(G) == 0:
    print('NO')
elif board[r2][c2] == 'X':
    board[r2][c2] = '.'
    if isConnected(r1, c1, r2, c2, board):
        print('YES')
    else:
        print('NO')
elif len(G) < 2:
    print('NO')
elif isConnected(r1, c1, r2, c2, board):
    print('YES')
else:
    print('NO')
