n, c = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [[0 for i in range(2)] for i in range(n + 1)]
dp[0][0] = 0
dp[0][1] = c
print(min(dp[0][0], dp[0][1]), end=" ")
for i in range(1, n):
    dp[i][0] = min(dp[i - 1][0] + a[i - 1], dp[i - 1][1] + a[i - 1])
    dp[i][1] = min(dp[i - 1][0] + c + b[i - 1], dp[i - 1][1] + b[i - 1])
    print(min(dp[i][0], dp[i][1]), end=" ")
