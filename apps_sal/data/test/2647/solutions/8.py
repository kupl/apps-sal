from collections import deque

H, W = list(map(int, input().split()))

mazo = [list(input()) for _ in range(H)]

cnt = 0
for i in range(H):
    for j in range(W):
        if mazo[i][j] == "
        cnt += 1

d = deque()
d.append((0, 0))

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = [[0] * W for _ in range(H)]

flg = False
while d:
    y, x = d.popleft()
    if (y == H - 1) and (x == W - 1):
        flg = True
        break

    for u, v in move:
        t = y + u
        s = x + v
        if 0 <= t and t < H and 0 <= s and s < W and mazo[t][s] == "." and visited[t][s] == 0:
            visited[t][s] = visited[y][x] + 1
            d.append((t, s))

if flg:
    print((H * W - cnt - visited[H - 1][W - 1] - 1))
else:
    print((-1))
