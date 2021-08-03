n = int(input())
grid = [[int(x) for x in input().split()] for _ in range(n)]

if n == 1:
    print(1)
    return

sm = sum(grid[1]) if 0 in grid[0] else sum(grid[0])

answer = -1
for i, line in enumerate(grid):
    if 0 in line:
        j = line.index(0)
        answer = sm - sum(line)
        grid[i][j] = answer
        break


for line in grid:
    if sum(line) != sum(grid[0]):
        print(-1)
        return

for i in range(n):
    row_count = 0
    for j in range(n):
        row_count += grid[j][i]

    if row_count != sum(grid[0]):
        print(-1)
        return

count = 0
for i in range(n):
    count += grid[i][i]

if count != sum(grid[0]):
    print(-1)
    return

count = 0
for i in range(n):
    count += grid[n - 1 - i][i]

if count != sum(grid[0]):
    print(-1)
    return

print(answer if answer > 0 else -1)
