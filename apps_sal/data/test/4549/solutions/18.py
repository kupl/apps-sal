(H, W) = map(int, input().split())
grid = [input() for _ in range(H)]
flg = True
for i in range(H):
    for j in range(W):
        if grid[i][j] == '.':
            continue
        flg2 = False
        if j > 0 and grid[i][j - 1] == '#':
            flg2 = True
        if j < W - 1 and grid[i][j + 1] == '#':
            flg2 = True
        if i > 0 and grid[i - 1][j] == '#':
            flg2 = True
        if i < H - 1 and grid[i + 1][j] == '#':
            flg2 = True
        if not flg2:
            flg = False
print(['No', 'Yes'][flg])
