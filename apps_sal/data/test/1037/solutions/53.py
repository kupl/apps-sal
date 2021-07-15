n = int(input())
a = [(_a, i) for i, _a in enumerate(map(int, input().split()))]
a.sort(reverse=True)

dp = [[0]*(n+1) for _ in range(n+1)]
for i, (v, p) in enumerate(a):
    # 前にj人いる
    dp[i+1][0] = dp[i][0] + v*abs((n-1 - i) - p)
    for j in range(1, i+1):
        dp[i+1][j] = max(dp[i][j] + v*abs((n-1 - (i-j)) - p),
                         dp[i][j-1] + v*abs((j-1) - p))
    dp[i+1][i+1] = dp[i][i] + v*abs(i - p)
print((max(dp[n])))

