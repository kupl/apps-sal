import numpy as np


def main():
    MOD = 998244353
    (N, S) = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    dp = np.zeros(S + 1, np.int64)
    dp[0] = 1
    for (i, a) in enumerate(A, start=1):
        dp_next = 2 * dp
        dp_next[a:] += dp[:-a]
        dp_next %= MOD
        dp = dp_next
    print(dp[S])


def __starting_point():
    main()


__starting_point()
