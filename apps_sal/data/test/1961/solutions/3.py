import sys


def solve(n, m, grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            must = cell == 1
            if i >= n - 2 or j >= m - 2:
                if must:
                    return 'NO'
                continue
            for di, dj in [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]:
                if grid[i + di][j + dj] == 0:
                    if must:
                        return 'NO'
                    break
            else:
                for di, dj in [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]:
                    grid[i + di][j + dj] = 2
                grid[i][j] = 2
    return 'YES'


n, m = list(map(int, input().split()))
grid = [['.
print(solve(n, m, grid))
