from collections import deque


def bfs():
    d = [[float('inf')] * w for i in range(h)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    que = deque([])
    que.append((sx, sy))
    d[sx][sy] = 0
    while que:
        p = que.popleft()
        if p[0] == gx and p[1] == gy:
            break
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            if 0 <= nx < h and 0 <= ny < w and (maze[nx][ny] != '#') and (d[nx][ny] == float('inf')):
                que.append((nx, ny))
                d[nx][ny] = d[p[0]][p[1]] + 1
    return d[gx][gy]


(h, w) = map(int, input().split())
maze = [list(input()) for i in range(h)]
(sx, sy) = (0, 0)
(gx, gy) = (h - 1, w - 1)
white = 0
for i in range(h):
    for j in range(w):
        if maze[i][j] == '.':
            white += 1
res = bfs()
if 0 < res < float('inf'):
    print(white - res - 1)
else:
    print(-1)
