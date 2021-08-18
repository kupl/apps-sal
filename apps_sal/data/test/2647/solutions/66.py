from collections import deque
H, W = map(int, input().split())
inf = 101
s = [''] * H
cnt = 0
for i in range(H):
    s[i] = input()
    cnt += s[i].count('.')
d = [[inf] * W for i in range(H)]
queue = deque([[0, 0]])
d[0][0] = 0

while queue:
    x, y = queue.popleft()
    if x + 1 == H and y + 1 == W:
        break
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx and nx < H and 0 <= ny and ny < W and s[nx][ny] != '
        queue.append([nx, ny])
        d[nx][ny] = d[x][y] + 1

if d[H - 1][W - 1] == inf:
    print(-1)
else:
    print(cnt - d[H - 1][W - 1] - 1)
