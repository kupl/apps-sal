n, m, Q = [int(i) for i in input().split()]
grid = [[0] * n for i in range(n)]
grid_acc = [[0] * n for i in range(n)]
for i in range(m):
    l, r = [int(i) for i in input().split()]
    grid[l - 1][r - 1] += 1

grid_acc[0][0] = grid[0][0]
for i in range(1, n):
    grid_acc[i][0] = grid_acc[i - 1][0] + grid[i][0]
    grid_acc[0][i] = grid_acc[0][i - 1] + grid[0][i]

for i in range(1, n):
    for j in range(1, n):
        grid_acc[i][j] = grid_acc[i - 1][j] + grid_acc[i][j - 1] - grid_acc[i - 1][j - 1] + grid[i][j]

for i in range(Q):
    p, q = [int(i) for i in input().split()]
    if p == 1:
        print((grid_acc[q - 1][q - 1]))
    else:
        print((grid_acc[q - 1][q - 1] - grid_acc[p - 2][q - 1] - grid_acc[q - 1][p - 2] + grid_acc[p - 2][p - 2]))
