N = input()
dp = [[0]*2 for _ in range(1001000)]
dp[0][1] = 1
for i in range(len(N)):
    d = int(N[i])
    dp[i+1][0] = min(dp[i][0] + d, dp[i][1] + 10-d)
    dp[i+1][1] = min(dp[i][0] + d + 1, dp[i][1] + 10-d-1)  # もらいすぎている状態を維持する
ans = dp[len(N)][0]
print(ans)

