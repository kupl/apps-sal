H, W = map(int, input().split())
grid = [input() for _ in range(H)]

cnt_y = [0] * H
cnt_x = [0] * W

for i in range(H):
    for j in range(W):
        if grid[i][j] == '.':
            cnt_y[i] += 1

for j in range(W):
    for i in range(H):
        if grid[i][j] == '.':
            cnt_x[j] += 1

for i in range(H):
    res = ''
    for j in range(W):
        if cnt_y[i] < W and cnt_x[j] < H:
            res += grid[i][j]
    if len(res) > 0:
        print(res)
