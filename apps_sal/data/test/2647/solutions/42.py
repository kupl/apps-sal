from collections import deque

H, W = map(int, input().split())
maze = [list(input()) for i in range(H)]

sx, sy = 0, 0
gx, gy = H - 1, W - 1


def bfs():
    d = [[float('inf')] * W for i in range(H)]
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
            if 0 <= nx < H and 0 <= ny < W and maze[nx][ny] != "#" and d[nx][ny] == float("inf"):
                que.append((nx, ny))
                d[nx][ny] = d[p[0]][p[1]] + 1

    return d[gx][gy]


ans = 0
cnt = 0
res = bfs()
for i in range(H):
    for j in range(W):
        if maze[i][j] == '.':
            cnt += 1
if res == float('inf'):
    ans = -1
else:
    ans = cnt - res - 1
print(ans)
