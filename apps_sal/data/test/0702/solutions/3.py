n = int(input().strip())
grid = [list(input().strip()) for _ in range(n)]
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if grid[i][j] == '.' and grid[i][j + 1] == '.' and grid[i][j - 1] == '.' and grid[i + 1][j] == '.' and grid[i - 1][j] == '.':
            grid[i][j] = '#'
            grid[i][j + 1] = '#'
            grid[i][j - 1] = '#'
            grid[i + 1][j] = '#'
            grid[i - 1][j] = '#'

for i in range(n):
    for j in range(n):
        if grid[i][j] == '.':
            print('NO')
            quit()

print('YES')
