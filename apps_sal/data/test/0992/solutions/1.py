import numpy as np

MOD = 998244353


def main():
    n, s = list(map(int, input().split()))
    a = list(map(int, input().split()))
    dp = np.zeros((n + 1, s + 1), dtype=np.int64)
    dp[0][0] = 1
    for i, v in enumerate(a):
        dp[i + 1] += dp[i] * 2
        if v <= s:
            dp[i + 1][v:] += dp[i][:-v]
        dp[i + 1] %= MOD
    print((int(dp[n][s]) % MOD))


def __starting_point():
    main()


__starting_point()
