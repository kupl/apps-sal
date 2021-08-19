from collections import deque
(H, W) = map(int, input().split())
S = [''] * H
for i in range(H):
    S[i] = input()
dests = ((-1, 0), (0, -1), (1, 0), (0, 1))


def maze(sx, sy):
    d = deque()
    dist = [[-1] * W for i in range(H)]
    dist[sx][sy] = 0
    d.append((sx, sy))
    while True:
        (x, y) = d.popleft()
        for dest in dests:
            (nx, ny) = (x + dest[0], y + dest[1])
            if nx >= 0 and nx < H and (ny >= 0) and (ny < W) and (S[nx][ny] == '.') and (dist[nx][ny] == -1):
                d.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
        if not d:
            return dist[x][y]


ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        ans = max(ans, maze(i, j))
print(ans)
