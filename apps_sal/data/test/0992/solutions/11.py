import numpy as np


def main():
    (n, s) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    dp = np.array([0 for i in range(min(3001, s + 1))])
    dp[0] = 1
    for ai in A:
        tmp = dp[:-ai].copy()
        dp *= 2
        dp[ai:] += tmp
        dp %= 998244353
    print(dp[s])


def __starting_point():
    main()


__starting_point()
