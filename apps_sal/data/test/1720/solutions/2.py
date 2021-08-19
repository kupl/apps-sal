from collections import deque
(n, m, k) = map(int, input().split())
INF = float('inf')
d = [[INF] * m for _ in range(n)]
t = [[] for i in range(n)]
for i in range(n):
    a = list(input())
    t[i] = a
(sx, sy, gx, gy) = map(int, input().split())
(sx, sy, gx, gy) = (sx - 1, sy - 1, gx - 1, gy - 1)


def bfs():
    que = deque()
    que.append((sx, sy))
    d[sx][sy] = 0
    while len(que):
        (x, y) = que.popleft()
        if x == gx and y == gy:
            break
        for (dx, dy) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            for i in range(1, k + 1):
                (nx, ny) = (x + i * dx, y + i * dy)
                if not 0 <= nx < n or not 0 <= ny < m or t[nx][ny] != '.' or (d[nx][ny] <= d[x][y]):
                    break
                elif d[nx][ny] > d[x][y] + 1:
                    d[nx][ny] = d[x][y] + 1
                    que.append((nx, ny))
    return d[gx][gy]


ans = bfs()
if ans == INF:
    print(-1)
else:
    print(ans)
