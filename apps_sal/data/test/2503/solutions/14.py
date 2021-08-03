import numpy as np

N, K = map(int, input().split())
p = [list(input().split()) for _ in range(N)]
grid = [[[0] * 2 for j in range(K)] for i in range(K)]

for i in range(N):
    x, y, c = p[i]
    x, y = int(x), int(y)
    mx, my = x % K, y % K
    f = False
    if (x // K) % 2 != (y // K) % 2:
        f = not f
    if c == "W":
        f = not f
    if f:
        grid[0][0][0] += 1
        grid[mx][0][0] -= 1
        grid[0][my][0] -= 1
        grid[mx][my][0] += 2
    else:
        grid[0][my][0] += 1
        grid[mx][0][0] += 1
        grid[mx][my][0] -= 2
    f = False
    if (x // K) % 2 != (y // K) % 2:
        f = not f
    if c == "B":
        f = not f
    if f:
        grid[0][0][1] += 1
        grid[mx][0][1] -= 1
        grid[0][my][1] -= 1
        grid[mx][my][1] += 2
    else:
        grid[0][my][1] += 1
        grid[mx][0][1] += 1
        grid[mx][my][1] -= 2
grid = np.array(grid)
grid = np.cumsum(grid, axis=0)
grid = np.cumsum(grid, axis=1)
print(int(np.max(grid)))
