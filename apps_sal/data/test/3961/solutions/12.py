n = int(input())
p = list(map(int, input().split()))
m = int(1e9 + 7)

dp = [0] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    dp[i] = (2 * dp[i - 1] - dp[p[i - 1] - 1] + 2) % m

print(dp[n])
