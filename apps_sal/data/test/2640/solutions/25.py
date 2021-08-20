import numpy as np
from copy import deepcopy


def main():
    (height, width) = list(map(int, input().split()))
    grid = [list(input()) for _ in range(height)]
    grid = (np.array(grid) == '.') * 1
    left = np.zeros((height, width), dtype=int)
    right = deepcopy(left)
    upper = deepcopy(left)
    down = deepcopy(left)
    for i in range(height):
        if i == 0:
            upper[i] = grid[i]
        else:
            upper[i] = (upper[i - 1] + 1) * grid[i]
    for i in range(width):
        if i == 0:
            left[:, i] = grid[:, i]
        else:
            left[:, i] = (left[:, i - 1] + 1) * grid[:, i]
    for i in range(width - 1, -1, -1):
        if i == width - 1:
            right[:, i] = grid[:, i]
        else:
            right[:, i] = (right[:, i + 1] + 1) * grid[:, i]
    for i in range(height - 1, -1, -1):
        if i == height - 1:
            down[i] = grid[i]
        else:
            down[i] = (down[i + 1] + 1) * grid[i]
    print(np.max(left + right + upper + down - 3))


def __starting_point():
    main()


__starting_point()
