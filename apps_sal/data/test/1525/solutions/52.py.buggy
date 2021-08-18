import sys

h, w, k = map(int, input().split())
mod = 10 ** 9 + 7
if w == 1:
    print(1)
    return
row = [0 for i in range(w + 1)]
row[0] = 1
row[1] = 1
for i in range(w - 1):
    row[i + 2] = row[i + 1] + row[i]

dp = [[0 for i in range(w)] for j in range(h + 1)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        if j == 0:
            dp[i + 1][j] = dp[i][j] * row[w - 1] + dp[i][j + 1] * row[w - 2]
            dp[i + 1][j] %= mod
        elif j == w - 1:
            dp[i + 1][j] = dp[i][j] * row[w - 1] + dp[i][j - 1] * row[w - 2]
            dp[i + 1][j] %= mod
        else:
            dp[i + 1][j] = dp[i][j - 1] * row[j - 1] * row[w - j - 1] + dp[i][j] * row[j] * row[w - j - 1] + dp[i][j + 1] * row[j] * row[w - j - 2]
            dp[i + 1][j] %= mod
print(dp[h][k - 1])
