import numpy as np


def main():
    H, W = list(map(int, input().split()))
    S = np.array([list(input()) for _ in range(H)]) == '.'

    up = np.zeros((H, W), dtype=int)
    down = np.zeros((H, W), dtype=int)
    left = np.zeros((H, W), dtype=int)
    right = np.zeros((H, W), dtype=int)

    for i in range(H - 1):
        up[i + 1, :] = (up[i, :] + 1) * S[i, :]
    for i in range(H - 1):
        down[H - 2 - i, :] = (down[H - 1 - i, :] + 1) * S[H - 1 - i, :]
    for i in range(W - 1):
        left[:, i + 1] = (left[:, i] + 1) * S[:, i]
    for i in range(W - 1):
        right[:, W - 2 - i] = (right[:, W - 1 - i] + 1) * S[:, W - 1 - i]

    print((((up + down + left + right) * S).max() + 1))


def __starting_point():
    main()


__starting_point()
