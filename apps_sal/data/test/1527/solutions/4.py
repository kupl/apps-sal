#!/usr/bin/env python3
from collections import deque

h, w = list(map(int, input().split()))
maze = [input() for _ in range(h)]
ans = 0


def bfs(sx, sy):
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    d = [[-1] * w for _ in range(h)]
    q = deque([])

    q.append((sx, sy))
    d[sx][sy] = 0
    ans = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] != "#" and d[nx][
                    ny] == -1:
                q.append((nx, ny))
                d[nx][ny] = d[x][y] + 1
                ans = max(ans, d[nx][ny])
    return ans


for i in range(h):
    for j in range(w):
        if maze[i][j] == ".":
            ans = max(ans, bfs(i, j))
print(ans)

