x, y = list(map(int, input().split()))
grid = []

for i in range(x):
    grid.append(list(map(int, input().split())))

mi = grid[0][0]
prints = []
for i in range(x):
    mi = min(mi, min(grid[i]))

if x > y:
    for k in range(mi):
        for i in range(1, y + 1):
            prints.append('col ' + str(i))
else:
    for k in range(mi):
        for i in range(1, x + 1):
            prints.append('row ' + str(i))

for i in range(x):
    for j in range(y):
        grid[i][j] -= mi

for i in range(x):
    while min(grid[i]) > 0:
        prints.append('row ' + str(i + 1))
        for j in range(y):
            grid[i][j] -= 1
for i in range(y):
    indy = []
    for ranind in range(x):
        indy.append(grid[ranind][i])
    mindy = min(indy)
    for ran2 in range(mindy):
        prints.append('col ' + str(i + 1))
        for j in range(x):
            grid[j][i] -= 1

ma = grid[0][0]
for i in range(x):
    ma = max(ma, max(grid[i]))
    if ma != 0:
        print('-1')
        quit()

print(len(prints))
print('\n'.join(prints))
