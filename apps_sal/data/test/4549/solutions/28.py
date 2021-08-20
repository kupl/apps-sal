(H, W) = map(int, input().split())
grid = []
for i in range(H):
    grid.append([s for s in input()])
fail_flg = False
for i in range(H):
    if fail_flg:
        break
    for j in range(W):
        r_ij = grid[i][j]
        if r_ij == '.':
            continue
        else:
            c_ij = 0
            if 0 <= i <= H - 1 and 1 <= j <= W - 1:
                if grid[i][j - 1] == '#':
                    c_ij += 1
            if 0 <= i <= H - 1 and 0 <= j <= W - 2:
                if grid[i][j + 1] == '#':
                    c_ij += 1
            if 1 <= i <= H - 1 and 0 <= j <= W - 1:
                if grid[i - 1][j] == '#':
                    c_ij += 1
            if 0 <= i <= H - 2 and 0 <= j <= W - 1:
                if grid[i + 1][j] == '#':
                    c_ij += 1
            if c_ij == 0:
                fail_flg = True
                break
if fail_flg:
    print('No')
else:
    print('Yes')
