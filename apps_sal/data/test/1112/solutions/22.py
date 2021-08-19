grid = []
for x in range(3):
    j = input().split()
    grid.append([int(i) for i in j])
s = [sum(i) for i in grid]
grid[0][0] = max(s) - s[0] + 1
grid[1][1] = max(s) - s[1] + 1
grid[2][2] = max(s) - s[2] + 1
diag = grid[0][0] + grid[1][1] + grid[2][2]
tr = sum(grid[0])
while tr > diag:
    grid[0][0] += 1
    grid[1][1] += 1
    grid[2][2] += 1
    diag = grid[0][0] + grid[1][1] + grid[2][2]
    tr = sum(grid[0])
for i in grid:
    print(' '.join([str(x) for x in i]))
