N = int(input())
A = list(map(int, input().split()))
dp = [[-10 ** 20 for i in range(3)] for j in range(N + 1)]
dp[0][1] = 0
dp[1][1] = 0
dp[1][2] = A[0]
for i in range(1, N):
    if i % 2 == 0:
        dp[i + 1][0] = max(dp[i - 1][0] + A[i], dp[i][0])
        dp[i + 1][1] = max(dp[i - 1][1] + A[i], dp[i][1])
        dp[i + 1][2] = dp[i - 1][2] + A[i]
    else:
        dp[i + 1][0] = max(dp[i - 1][0] + A[i], dp[i][1])
        dp[i + 1][1] = max(dp[i - 1][1] + A[i], dp[i][2])
        dp[i + 1][2] = dp[i - 1][2] + A[i]
ans = dp[N][1]
print(ans)
