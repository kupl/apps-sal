(H, W) = map(int, input().split())
f = []
for _ in range(H):
    f.append(list(input()))
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
for h in range(H):
    for w in range(W):
        if f[h][w] == '#':
            continue
        cnt = 0
        for i in range(8):
            nw = w + dx[i]
            nh = h + dy[i]
            if nw < 0 or W <= nw or nh < 0 or (H <= nh):
                continue
            if f[nh][nw] == '#':
                cnt += 1
        f[h][w] = str(cnt)
for row in f:
    print(''.join(row))
