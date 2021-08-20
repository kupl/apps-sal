p = 1
n = int(input())
grid = []
for i in range(0, n):
    grid.append(input())
difx = (1, -1, 0, 0)
dify = (0, 0, -1, 1)
for i in range(0, n):
    for j in range(0, n):
        count = 0
        for c in range(0, 4):
            x = i + difx[c]
            y = j + dify[c]
            if x < 0 or x >= n or y < 0 or (y >= n):
                continue
            if grid[x][y] == 'o':
                count += 1
        if count % 2 != 0:
            p = 0
if p == 1:
    print('YES')
else:
    print('NO')
