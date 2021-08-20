import sys
import numpy as np


def read():
    return sys.stdin.readline().rstrip()


def main():
    (h, w) = list(map(int, read().split()))
    s = np.array([[i == '.' for i in read()] for _ in range(h)], dtype=int)
    left = np.zeros((h, w), dtype=int)
    right = np.zeros((h, w), dtype=int)
    up = np.zeros((h, w), dtype=int)
    down = np.zeros((h, w), dtype=int)
    left[:, 0] = s[:, 0]
    right[:, -1] = s[:, -1]
    for i in range(w - 1):
        left[:, i + 1] = (left[:, i] + 1) * s[:, i + 1]
        right[:, -i - 2] = (right[:, -i - 1] + 1) * s[:, -i - 2]
    up[0] = s[0]
    down[-1] = s[-1]
    for i in range(h - 1):
        up[i + 1] = (up[i] + 1) * s[i + 1]
        down[-i - 2] = (down[-i - 1] + 1) * s[-i - 2]
    print((left + right + up + down).max() - 3)


def __starting_point():
    main()


__starting_point()
