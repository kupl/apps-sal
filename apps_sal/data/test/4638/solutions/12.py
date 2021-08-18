n, c = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))

dp = [[0] * 2 for _ in range(n + 1)]
dp[1][0] = 0
dp[1][1] = c
for i in range(2, n + 1):
    dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + a[i - 1]
    dp[i][1] = min(dp[i - 1][0] + c, dp[i - 1][1]) + b[i - 1]

print(*[min(u) for u in dp][1:])
