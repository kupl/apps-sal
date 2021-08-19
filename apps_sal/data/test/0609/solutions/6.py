n = int(input())
grid = []
for i in range(n):
    grid.append(input())
x = grid[0][0]
o = grid[0][1]
if x == o:
    print('NO')
else:
    fine = True
    for i in range(n):
        if fine:
            for j in range(n):
                if j == i or j == n - 1 - i:
                    if grid[i][j] != x:
                        print('NO')
                        fine = False
                        break
                elif grid[i][j] != o:
                    print('NO')
                    fine = False
                    break
    if fine:
        print('YES')
