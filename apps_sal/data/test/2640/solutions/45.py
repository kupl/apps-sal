import numpy as np


def main():
    h, w = list(map(int, input().split()))
    s = np.array([[i == "." for i in input()] for _ in range(h)], dtype=int)
    left = s.copy()
    right = s.copy()
    up = s.copy()
    down = s.copy()
    for i in range(w - 1):
        left[:, i + 1] = (left[:, i] + 1) * s[:, i + 1]
        right[:, -i - 2] = (right[:, -i - 1] + 1) * s[:, -i - 2]
    for i in range(h - 1):
        up[i + 1] = (up[i] + 1) * s[i + 1]
        down[-i - 2] = (down[-i - 1] + 1) * s[-i - 2]
    print(((left + right + up + down).max() - 3))


def __starting_point():
    main()

__starting_point()
