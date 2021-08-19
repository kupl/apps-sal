def main():
    import sys
    sys.setrecursionlimit(10 ** 9)
    input = sys.stdin.readline
    import numpy as np
    (N, S) = map(int, input().split())
    A = list(map(int, input().split()))
    MOD = 998244353
    dp = np.zeros(S + 1, dtype='int32')
    dp[0] = 1
    for i in range(N):
        p = dp * 2 % MOD
        p[A[i]:] += dp[:-A[i]]
        dp = p % MOD
    print(dp[S])


main()
