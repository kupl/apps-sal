import numpy as np
MOD = 998244353

def main():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    dp = np.zeros((n+1, s+1), dtype=np.int64)
    dp[0][0] = 1
    for i in range(n):
        dp[i][dp[i] >= MOD] %= MOD
        dp[i+1] += dp[i]*2
        if a[i] <= s:
            dp[i+1][a[i]:] += dp[i][:-a[i]]
    print(dp[n][s]%MOD)

def __starting_point():
    main()
__starting_point()
