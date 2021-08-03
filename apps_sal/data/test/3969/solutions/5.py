n, m = map(int, input().split())
type = [0]
for x in range(n):
    type.append(int(input().split()[0]))

dp = [[0] * (m + 1) for x in range(2)]
for i in range(1, n + 1):
    dp[i & 1][0] = 1e9
    for j in range(1, m + 1):
        if type[i] == j:
            dp[i & 1][j] = dp[1 - (i & 1)][j]
        elif type[i] > j:
            dp[i & 1][j] = 1 + dp[1 - (i & 1)][j]
        else:
            if j >= 1:
                dp[i & 1][j] = min(dp[i & 1][j - 1], 1 + dp[1 - (i & 1)][j])
            else:
                dp[i & 1][j] = dp[1 - (i & 1)][j]
print(dp[n & 1][m])
