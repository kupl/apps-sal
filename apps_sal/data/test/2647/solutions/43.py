from collections import deque
H, W = map(int, input().split())
G = [input() for _ in range(H)]
sy, sx, gy, gx = 0, 0, H - 1, W - 1
seen = [[-1] * W for _ in range(H)]

if G[sy][sx] == '#' or G[gy][gx] == '#':
    print(-1)
    return

que = deque()
que.append([sy, sx])
seen[sy][sx] = 0
while que:
    y, x = que.popleft()
    for d in [-1, 0], [1, 0], [0, -1], [0, 1]:
        dy = y + d[0]
        dx = x + d[1]
        if dy < 0 or H <= dy or dx < 0 or W <= dx:
            continue
        if G[dy][dx] == '#':
            continue
        if seen[dy][dx] > -1:
            continue
        que.append([dy, dx])
        seen[dy][dx] = seen[y][x] + 1

count = 0
bunpu = [0] * (H * W + 1)
if seen[gy][gx] == -1:
    print(-1)
    return
else:
    all = H * W
    black = 0
    for i in range(H):
        for j in range(W):
            if G[i][j] == '#':
                black += 1
    # start point = 0,0
    ans = all - black - seen[gy][gx] - 1
print(ans)
