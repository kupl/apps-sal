(n, k) = list(map(int, input().split()))
num = list(map(int, input().split()))
dp = [0] * (2 * n)
for i in range(n - 1, -1, -1):
    dp[i] = dp[i + k] + num[i]
ans = 2 ** 100
for i in range(0, k):
    ans = min(ans, dp[i])
print(dp.index(ans) + 1)
