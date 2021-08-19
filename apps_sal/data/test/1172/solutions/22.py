s = input()
n = len(s)
p = 10 ** 9 + 7

# i = 0, ..., nについて
# dp[i][0] = i文字目まででありうる文字列の数（ABCなら1、AB?なら3）
# dp[i][1] = i文字目までに含まれるAの数
# dp[i][2] = i文字目までに含まれるABのパターン数
# dp[i][3] = i文字目までに含まれるABCのパターン数
dp = [[0 for j in range(4)] for i in range(n + 1)]
dp[0][0] = 1  # ''空の文字列は1パターン
for j in range(1, 4):
    dp[0][j] = 0  # 空の文字列にはAもABもABCも入っていない

for i in range(1, n + 1):
    m = 3 if s[i - 1] == '?' else 1

    for j in range(4):
        dp[i][j] = dp[i - 1][j] * m % p

    if s[i - 1] == 'A' or s[i - 1] == '?':
        dp[i][1] = (dp[i][1] + dp[i - 1][0]) % p
    if s[i - 1] == 'B' or s[i - 1] == '?':
        dp[i][2] = (dp[i][2] + dp[i - 1][1]) % p
    if s[i - 1] == 'C' or s[i - 1] == '?':
        dp[i][3] = (dp[i][3] + dp[i - 1][2]) % p

print(dp[n][3])
