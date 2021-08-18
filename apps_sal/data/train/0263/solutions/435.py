from functools import reduce


def make_grid():
    g = [[1] * 3 for _ in range(4)]
    g[3][0] = None
    g[3][2] = None
    return g


MOVES = [
    (2, 1),
    (2, -1),
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2),
    (-2, 1),
    (-2, -1),
]


def jump(grid):
    new_grid = make_grid()
    for i in range(4):
        for j in range(3):
            if grid[i][j] is not None:
                c = 0
                for di, dj in MOVES:
                    ni = i + di
                    nj = j + dj
                    if (0 <= ni < 4) and (0 <= nj < 3) and (grid[ni][nj] is not None):
                        c += grid[ni][nj]
                new_grid[i][j] = c
    return new_grid


class Solution:
    def knightDialer(self, n: int) -> int:

        grid = make_grid()
        m = 10**9 + 7

        c = 0
        for _ in range(n - 1):
            grid = jump(grid)
            c += 10

        print(grid)

        return sum([sum([c for c in row if c]) for row in grid]) % m
