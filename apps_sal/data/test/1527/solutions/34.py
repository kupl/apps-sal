from copy import deepcopy
from collections import deque
from itertools import product
import numpy as np


class Grid:
    def __init__(self, grid, w=0, h=0, function=lambda x: x):
        self.w = w = w if w else len(grid[0])
        self.h = h = h if h else len(grid)
        dtype = type(function(grid[0][0]))
        self.grid = np.empty((h, w), dtype=dtype)
        for i, row in zip(range(h), grid):
            for j, val in zip(range(w), row):
                self.grid[i][j] = function(val)

    def is_valid_x(self, x):
        return 0 <= x < self.w

    def is_valid_y(self, y):
        return 0 <= y < self.h

    def is_valid_xy(self, x, y):
        return self.is_valid_x(x) and self.is_valid_y(y)

    def __iter__(self):
        return iter(self.grid)

    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.grid]) + '\n'

    def __getitem__(self, x):
        return self.grid[x]

    def __setitem__(self, x, val):
        self.grid[x] = val


def longest_path(grid, root):
    def restore_path(prev, p):
        A = deque()
        while p:
            A.appendleft(p)
            p = prev[p]
        return list(A)

    x, y = root
    prev = {root: None}
    grid[y, x] = '!'
    queue = deque([root])
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
            nx, ny = x + dx, y + dy
            if grid.is_valid_xy(nx, ny) and grid[ny, nx] in 'sg.':
                prev[nx, ny] = x, y
                queue.append((nx, ny))
                grid[ny, nx] = '!'
    return restore_path(prev, (x, y))


h, w = map(int, input().split())
grid = Grid([input() for s in range(h)])
ans = 0
for y, x in product(range(h), range(w)):
    if grid[y, x] == '.':
        path = longest_path(deepcopy(grid), (x, y))
        ans = max(ans, len(path) - 1)
print(ans)
