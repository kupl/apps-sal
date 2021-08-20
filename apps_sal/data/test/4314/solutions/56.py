(H, W) = map(int, input().split())
row = [False] * H
col = [False] * W
grid = []
for i in range(H):
    grid.append(input())
for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            row[i] = True
            col[j] = True
for i in range(H):
    if not row[i]:
        continue
    for j in range(W):
        if not col[j]:
            continue
        print(grid[i][j], end='')
    print()
