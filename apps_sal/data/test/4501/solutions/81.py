n, a = map(int, input().split())
xlst = list(map(int, input().split()))
dp = [[0 for _ in range(5001)] for _ in range(n + 1)]
center = 2500
dp[0][center] = 1
for i, x in enumerate(xlst, 1):
    num = x - a
    for j in range(5001):
        dp[i][j] = dp[i - 1][j]
        if 0 <= j - num <= 5000:
            dp[i][j] += dp[i - 1][j - num]
print(dp[-1][center] - 1)
