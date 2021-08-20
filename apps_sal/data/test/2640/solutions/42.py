def main():
    import numpy as np
    (h, w) = map(int, input().split())
    grid = np.array([list(input()) for i in range(h)])
    grid = np.where(grid == '.', 1, 0)
    left = np.zeros((h, w), dtype=np.int64)
    right = np.zeros((h, w), dtype=np.int64)
    up = np.zeros((h, w), dtype=np.int64)
    down = np.zeros((h, w), dtype=np.int64)
    for i in range(w):
        left[:, i] = (left[:, i - 1] + 1) * grid[:, i]
        right[:, -i - 1] = (right[:, -i] + 1) * grid[:, -i - 1]
    for i in range(h):
        up[i] = (up[i - 1] + 1) * grid[i]
        down[-i - 1] = (down[-i] + 1) * grid[-i - 1]
    print(np.max(left + right + up + down) - 3)


def __starting_point():
    main()


__starting_point()
