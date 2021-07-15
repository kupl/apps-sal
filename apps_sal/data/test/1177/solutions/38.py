import numpy as np
MOD = 998244353
def main():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [np.zeros(s+1, dtype=np.int64) for i in range(n+1)]
    ans = 0
    for i in range(n):
        if a[i] <= s:
            dp[i+1][a[i]:] = dp[i][:-a[i]]
            dp[i+1][a[i]] += i+1
        dp[i+1][:s] += dp[i][:s]
        dp[i+1][dp[i+1] >= MOD] -= MOD
        ans += dp[i+1][s] * (n-i)
        ans %= MOD
#        print(dp[i+1], ans)
    print(ans)

def __starting_point():
    main()
__starting_point()
