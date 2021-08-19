#import sys
#input = sys.stdin.buffer.readline
import numpy as np


def main():
    H, W = list(map(int, input().split()))
    S = np.array([list(input()) for _ in range(H)]) == '.'  # '.'に一致するならTrueしなければFalse

    up = np.zeros((H, W), dtype=int)
    down = np.zeros((H, W), dtype=int)
    left = np.zeros((H, W), dtype=int)
    right = np.zeros((H, W), dtype=int)

    for i in range(H - 1):
        up[i + 1, :] = (up[i, :] + 1) * S[i, :]  # npの変数名[k,l]でk行l列を取り出す
    for i in range(H - 1):  # :なら全部をそれぞれについて見ていく
        down[H - 2 - i, :] = (down[H - 1 - i, :] + 1) * S[H - 1 - i, :]
    for i in range(W - 1):
        left[:, i + 1] = (left[:, i] + 1) * S[:, i]
    for i in range(W - 1):
        right[:, W - 2 - i] = (right[:, W - 1 - i] + 1) * S[:, W - 1 - i]

    print((((up + down + left + right) * S).max() + 1))  # カケザンデ要素ごとの掛け算可能


def __starting_point():
    main()


__starting_point()
