n = int(input())
s = input()
t = 'hard'
a = list(map(int, input().split()))
dp = [x[:] for x in [[0] * 4] * (n + 1)]
for i in range(1, n + 1):
    for j in range(4):
        if s[i - 1] == t[j]:
            if j == 0:
                dp[i][j] = dp[i - 1][j] + a[i - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + a[i - 1], dp[i - 1][j - 1])
        else:
            dp[i][j] = dp[i - 1][j]
res = float('inf')
for i in range(4):
    res = min(res, dp[n][i])
print(res)
