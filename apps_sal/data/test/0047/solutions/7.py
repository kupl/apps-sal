(n, x) = list(map(int, input().split()))
arr = [int(x) for x in input().split()]
dp = [[0 for _ in range(n)] for _ in range(3)]
dp[0][0] = max(arr[0], 0)
dp[1][0] = max(arr[0] * x, 0)
dp[2][0] = max(arr[0], 0)
answer = max(dp[0][0], dp[1][0], dp[2][0])
for i in range(1, n):
    dp[0][i] = max(dp[0][i - 1] + arr[i], arr[i], 0)
    dp[1][i] = max(dp[0][i - 1] + arr[i] * x, dp[1][i - 1] + arr[i] * x, arr[i] * x, 0)
    dp[2][i] = max(dp[1][i - 1] + arr[i], dp[2][i - 1] + arr[i], arr[i], 0)
    answer = max(answer, dp[0][i], dp[1][i], dp[2][i])
print(answer)
