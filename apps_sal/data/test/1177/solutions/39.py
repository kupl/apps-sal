import numpy as np

MOD = 998244353

def main():
    n, s = list(map(int, input().split()))
    a = list(map(int, input().split()))
    dp = np.zeros((n+1, s+1), dtype=np.int64)
    for i, v in enumerate(a):
        dp[i][0] += 1
        dp[i+1] += dp[i]
        if v <= s:
            dp[i+1][v:] += dp[i][:-v]
        dp[i+1] %= MOD
    ans = 0
    for i in range(n+1):
        ans += dp[i][s]
        ans %= MOD
    print(ans)

def __starting_point():
    main()

__starting_point()
