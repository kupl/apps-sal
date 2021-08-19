(H, W) = map(int, input().split())
grid = [input().split() for _ in range(H)]
check = []
for i in range(H):
    if '#' not in grid[i][0]:
        check.append(i - len(check))
for i in check:
    grid = grid[:i] + grid[i + 1:]
check = []
for i in range(W):
    if all((grid[j][0][i] == '.' for j in range(len(grid)))):
        check.append(i - len(check))
for i in check:
    for k in range(len(grid)):
        grid[k][0] = grid[k][0][:i] + grid[k][0][i + 1:]
for i in grid:
    print(i[0])
