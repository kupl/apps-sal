import numpy as np


def main():
    (H, W) = list(map(int, input().split(' ')))
    field = np.array([list(input()) for _ in range(H)])
    field = np.where(field == '#', 0, 1)
    (left, right, up, down) = [np.zeros((H, W)) for _ in range(4)]
    for w in range(W):
        left[:, w] = (left[:, w - 1] + 1) * field[:, w]
        right[:, -w - 1] = (right[:, -w] + 1) * field[:, -w - 1]
    for h in range(H):
        up[h, :] = (up[h - 1, :] + 1) * field[h, :]
        down[-h - 1, :] = (down[-h, :] + 1) * field[-h - 1, :]
    s = left + right + up + down - 3
    print(int(np.max(s)))


def __starting_point():
    main()


__starting_point()
