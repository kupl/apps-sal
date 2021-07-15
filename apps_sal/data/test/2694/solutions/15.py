intput = lambda: [int(i) for i in input().split()]
# Write your code here
n, m, k = intput()
blasters = [intput() for i in range(k)]
grid = [[1] * n for i in range(m)]

for bx, by, t, f in blasters:
    bx -= 1
    by -= 1
    
    for x in range(n):
        k = x + by - abs(bx - x) - t
        if k >= 0 and k % f == 0:
            grid[by][x] = 0
    
    for y in range(m):
        k = bx + y - abs(by - y) - t
        if k >= 0 and k % f == 0:
            grid[y][bx] = 0
    
for x in range(1, n):
    grid[0][x] = grid[0][x] and grid[0][x - 1]
for y in range(1, m):
    grid[0][y] = grid[0][y] and grid[0][y - 1]

for x in range(1, n):
    for y in range(1, m):
        grid[y][x] = grid[y][x] and (grid[y][x - 1] or grid[y - 1][x])
    
if grid[-1][-1]:
    print('YES')
    print(n + m - 2)
else:
    print('NO')
