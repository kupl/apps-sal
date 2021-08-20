from sys import stdin
import numpy as np


def main():
    readline = stdin.readline
    (h, n) = map(int, readline().split())
    ab = np.array([list(map(int, readline().split())) for _ in range(n)], dtype=np.int64)
    a = ab[:, 0]
    b = ab[:, 1]
    dp = np.zeros(h + 1, dtype=np.int64)
    for i in range(1, h + 1):
        dp[i] = (dp[np.maximum(0, i - a)] + b).min()
    print(dp[h])


def __starting_point():
    main()


__starting_point()
