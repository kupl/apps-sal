n, m = list(map(int, input().split()))
grid = []
for _ in range(n):
    grid.append([c for c in input()])

top = n
bot = -1
left = m
right = -1
for row in range(n):
    for col in range(m):
        if grid[row][col] == 'X':
            top = min(top, row)
            bot = max(row, bot)
            left = min(col, left)
            right = max(col, right)

fail = False
for row in range(top, bot + 1):
    for col in range(left, right + 1):
        if grid[row][col] != 'X':
            fail = True
print('NO' if fail else 'YES')
