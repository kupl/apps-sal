n = int(input())

grid = []

for i in range(n):
    grid.append(list(map(int, input().split())))

if n == 1:
    print(1)
    return

checksum = -1

left = 0
mis = -1
for i, col in enumerate(grid):
    tmp = sum(col)
    if 0 in col:
        left = i
        mis = tmp
    else:
        if checksum == -1:
            checksum = tmp
        elif checksum != tmp:
            print(-1)
            return

if mis >= checksum:
    print(-1)
    return

grid[left] = [x if x else checksum - mis for x in grid[left]]

diag1 = 0
diag2 = 0
for i in range(n):
    colsum = 0
    rowsum = 0
    diag1 += grid[i][i]
    diag2 += grid[n - 1 - i][i]
    for j in range(n):
        colsum += grid[i][j]
        rowsum += grid[j][i]

    if colsum != checksum or rowsum != checksum:
        print(-1)
        return

if diag1 != checksum or diag2 != checksum:
    print(-1)
    return

print(checksum - mis)
