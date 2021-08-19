n = int(input())
A = list(map(int, input().split()))
dp = [[0] * 2 for _ in range(n)]
for i in range(n - 1):
    if i == 0:
        dp[i + 1][0] += A[i]
        dp[i + 1][1] += -A[i]
    else:
        dp[i + 1][0] = max(dp[i][0] + A[i], dp[i][1] + -1 * A[i])
        dp[i + 1][1] = max(dp[i][0] + -1 * A[i], dp[i][1] + A[i])
ans = max(dp[n - 1][0] + A[n - 1], dp[n - 1][1] + -1 * A[n - 1])
print(ans)
