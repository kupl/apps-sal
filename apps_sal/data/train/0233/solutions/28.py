from itertools import chain
class Solution:
    def regionsBySlashes(self, grid):
        grid = convert_grid(grid)
        return len([destroy_island(x, y, grid) for y in range(len(grid)) for x,v in enumerate(grid[y]) if v == 0])

def destroy_island(x, y, grid):
    grid[y][x] = 1
    for c in search(x, y, grid):
        destroy_island(c[0], c[1], grid)

def search(x, y, grid):
    in_bounds = lambda c:0 <= c[1] < len(grid) and 0 <= c[0] < len(grid[c[1]])
    check_orthog = lambda c:in_bounds(c) and grid[c[1]][c[0]] == 0
    def check_diag(c):
        if not in_bounds(c) or grid[c[1]][c[0]] != 0: return False
        d_x, d_y = c[0] - x, c[1] - y
        sep = '\\\\' if ((d_x > 0 > d_y) or (d_x < 0 < d_y)) else '/'
        return not (grid[y + d_y][x] == sep and grid[y][x + d_x] == sep)
    yield from chain(filter(check_orthog, ((x-1, y), (x+1, y), (x, y-1), (x, y+1))),
                     filter(check_diag, ((x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1))))

def convert_grid(grid):
    new_grid = [[0] * len(grid[0]) * 2 for _ in range(len(grid) * 2)]
    for (x, y, v) in ((x, y, v) for y in range(len(grid)) for x,v in enumerate(grid[y]) if v in '\\\\/'):
        new_grid[y * 2 + 0][x * 2 + (1 if v == '/' else 0)] = v
        new_grid[y * 2 + 1][x * 2 + (0 if v == '/' else 1)] = v
    return new_grid
