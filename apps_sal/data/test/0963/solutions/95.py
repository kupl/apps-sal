(n, k) = list(map(int, input().split()))
dp = [0] * n
a = [list(map(int, input().split())) for i in range(k)]
dp[0] = 1
dp[1] = -1
for i in range(n - 1):
    for (l, r) in a:
        if i + l < n:
            dp[i + l] += dp[i]
    for (l, r) in a:
        if i + r + 1 < n:
            dp[i + r + 1] -= dp[i]
    dp[i + 1] += dp[i]
    dp[i + 1] %= 998244353
print(dp[n - 1])
