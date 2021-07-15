import numpy as np
import sys
input = sys.stdin.readline


def main():
    n, s = map(int, input().split())
    A = [int(i) for i in input().split()]

    MOD = 998244353

    dp = np.zeros(s + 1, dtype="int32")
    dp[0] = 1

    for a in A:
        p = (dp * 2) % MOD
        p %= MOD
        p[a:] += dp[:-a]
        dp = p % MOD

    print(dp[s])


def __starting_point():
    main()
__starting_point()
