R = lambda: map(int, input().split())
n = int(input())
unset = -1000000
bs = [[0, 0]] + [list(R()) for i in range(n)]
dp = [[unset] * 201 for i in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    for j in range(201):
        t, w = bs[i + 1][0], bs[i + 1][1]
        if dp[i][j] != unset:
            dp[i + 1][j + t] = max(dp[i + 1][j + t], dp[i][j] + t)
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] - w)
for i in range(201):
    if dp[n][i] >= 0:
        print(i)
        break
