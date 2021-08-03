N, A, B = map(int, input().split())
vlist = list(map(int, input().split()))
# vlist.sort(reverse=True)

dp = [[(-1, -1)] * (N + 1) for _ in range(N + 1)]
dp[0][0] = (0, 1)

for i in range(1, N + 1):
    dp[i][0] = (0, 1)
    for j in range(1, i + 1):
        dp[i][j] = dp[i - 1][j]
        if dp[i - 1][j - 1][0] + vlist[i - 1] > dp[i][j][0]:
            dp[i][j] = (dp[i - 1][j - 1][0] + vlist[i - 1], dp[i - 1][j - 1][1])
        elif dp[i - 1][j - 1][0] + vlist[i - 1] == dp[i][j][0]:
            dp[i][j] = (dp[i][j][0], dp[i][j][1] + dp[i - 1][j - 1][1])
# print(dp)

max_value_avg = 0
for j in range(A, B + 1):
    # print(j,dp[N][j])
    value_avg = dp[N][j][0] / j
    max_value_avg = max(max_value_avg, value_avg)

answer = 0
for j in range(A, B + 1):
    value_avg = dp[N][j][0] / j
    if value_avg == max_value_avg:
        answer += dp[N][j][1]

print(max_value_avg)
print(answer)
