(n, m) = map(int, input().split())
mod = 10 ** 9 + 7
dp = [-1] * (n + 1)
dp[0] = 0
dp[1] = 1
for i in range(m):
    a = int(input())
    dp[a] = 0
for i in range(2, n + 1):
    if dp[i] == -1:
        if i <= 2:
            dp[i] = dp[i - 1] + 1
        elif i >= 3:
            dp[i] = (dp[i - 1] + dp[i - 2]) % mod
print(dp[n])
