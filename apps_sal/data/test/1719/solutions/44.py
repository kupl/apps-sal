n = int(input())
dp = [[0] * 4 for i in range(n + 2)]  # dp[i][j]=(長さiの最後の文字がjで条件を満たす文字列の数:j= 0:A 1:G 2:C 3:T)
# 番兵を2つ置いておくと都合がいい
for i in range(4):
    dp[2][i] = 1
mod = 10**9 + 7
for i in range(3, n + 2):
    for j in range(4):
        for k in range(4):
            dp[i][j] += dp[i - 1][k]
    dp[i][2] -= dp[i - 2][0] # AGCを取り除く.
    dp[i][2] -= dp[i - 2][1] # GACを取り除く.
    dp[i][1] -= dp[i - 2][0] - dp[i - 3][1] # ACGを取り除く. ただしGACGはすでに取り除いている.
    dp[i][2] -= 3 * dp[i - 3][0] # すでに取り除いているものに注意する.結果的にAGGC,ATGC,AGTCを取り除く.
print(sum(dp[-1]) % mod)
