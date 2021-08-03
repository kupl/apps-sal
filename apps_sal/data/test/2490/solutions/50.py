n = input()
n = n[::-1] + '0'
inf = 10 ** 9
dp = [[inf for _ in range(2)] for _ in range(len(n) + 1)]
dp[0][0] = 0
dp[0][1] = 2
for i in range(len(n)):
    n_i = int(n[i])
    dp[i + 1][0] = min(dp[i][0] + n_i, dp[i][1] + n_i)
    dp[i + 1][1] = min(dp[i][0] + 11 - n_i, dp[i][1] + 9 - n_i)
print(min(dp[-1][0], dp[-1][1]))
