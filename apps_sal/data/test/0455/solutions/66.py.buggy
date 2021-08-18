n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]

for i in range(n - 1):
    if (grid[i][0] + grid[i][1]) % 2 != (grid[i + 1][0] + grid[i + 1][1]) % 2:
        print(-1)
        return
m = 31
D = [2 ** i for i in range(m)]
if (grid[0][0] + grid[0][1]) % 2 == 0:
    D.insert(0, 1)
    m += 1
w = [[] for i in range(n)]
for i, g in enumerate(grid):
    x, y = g
    for d in D[::-1]:
        if abs(x) >= abs(y):
            if x > 0:
                x -= d
                w[i].append('R')
            else:
                x += d
                w[i].append('L')
        else:
            if y > 0:
                y -= d
                w[i].append('U')
            else:
                y += d
                w[i].append('D')

print(m)
print(*D)
for ans in w:
    print(*ans[::-1], sep='')
