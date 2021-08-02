n, m = map(int, input().split())
dp = [0] * (n + 1)
for _ in range(m):
    a = int(input())
    dp[a] = -1
dp[0] = 1
for i in range(0, n):
    if dp[i] < 0:
        continue
    dp[i] %= 1000000007
    if dp[i + 1] >= 0:
        dp[i + 1] += dp[i]
    if i != (n - 1):
        if dp[i + 2] >= 0:
            dp[i + 2] += dp[i]
print(dp[n] % 1000000007)
