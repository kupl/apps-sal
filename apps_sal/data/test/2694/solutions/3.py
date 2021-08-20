(n, m, k) = map(int, input().split())
blasters = []
for _ in range(k):
    blasters.append(list(map(int, input().split())))
grid = [[0 for _ in range(m)] for _ in range(n)]
for blaster in blasters:
    (x, y, t, f) = blaster
    x -= 1
    y -= 1
    grid[x][y] = -1
    for i in range(n):
        if (i + y - t) % f == abs(x - i):
            grid[i][y] = -1
    for j in range(m):
        if (j + x - t) % f == abs(y - j):
            grid[x][j] = -1
for i in range(1, n):
    if grid[i - 1][0] == -1:
        grid[i][0] = -1
for j in range(1, m):
    if grid[0][j - 1] == -1:
        grid[0][j] = grid[0][j - 1]
for i in range(1, n):
    for j in range(1, m):
        if grid[i][j - 1] == -1 and grid[i - 1][j] == -1:
            grid[i][j] = -1
if grid[-1][-1] == 0:
    print('YES')
    print(n + m - 2)
else:
    print('NO')
