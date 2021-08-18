import copy
H, W = map(int, input().split())
MAZE = [0] * H
for i in range(H):
    MAZE[i] = list(str(input()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def solve_maze(sy, sx):
    MAZE1 = copy.deepcopy(MAZE)
    MAZE1[sy][sx] = '
    queue = []
    queue.append([sy, sx])
    d = [[100000000] * W for i in range(H)]
    d[sy][sx] = 0
    while len(queue) > 0:
        Q = queue.pop(0)
        move = d[Q[0]][Q[1]]

        for j in range(4):
            y = Q[0] + dy[j]
            x = Q[1] + dx[j]
            if 0 <= y <= (H - 1) and 0 <= x <= (W - 1) and MAZE1[y][x] == '.':
                queue.append([y, x])
                MAZE1[y][x] = '
                d[y][x] = move + 1
    return move


d_max = 0
for i in range(H):
    for j in range(W):
        if MAZE[i][j] == '.':
            d = solve_maze(i, j)
            if d > d_max:
                d_max = d
print(d_max)
