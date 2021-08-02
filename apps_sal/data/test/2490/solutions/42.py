n = input()
x = len(n)
inf = 10 ** 9
# dp[i][flg]...i桁目まで、未満フラグ=1
dp = [[inf] * 2 for _ in range(x + 1)]
dp[0][0] = 0
dp[0][1] = 1
for i in range(x):
    s = int(n[i])
    dp[i + 1][0] = min(dp[i][0] + s, dp[i][1] + 10 - s)
    dp[i + 1][1] = min(dp[i][0] + s + 1, dp[i][1] + 9 - s)

print((dp[x][0]))
