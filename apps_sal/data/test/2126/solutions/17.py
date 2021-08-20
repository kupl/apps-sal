import sys
input = sys.stdin.readline
(n, m, h) = map(int, input().split())
front = list(map(int, input().split()))
left = list(map(int, input().split()))
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            grid[i][j] = min(front[j], left[i])
for row in grid:
    print(' '.join([str(x) for x in row]))
