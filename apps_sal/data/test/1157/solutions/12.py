n = int(input())
l = [int(s) for s in input().split()]
dp = [[0, 0] for i in range(n)]
if l[0] < 0:
    dp[0][0] = 1
else:
    dp[0][1] = 1
for i in range(1, n):
    if l[i] < 0:
        dp[i][0] = dp[i - 1][1] + 1
        dp[i][1] = dp[i - 1][0]
    else:
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = dp[i - 1][1] + 1
ans1 = sum([i[0] for i in dp])
ans2 = sum([i[1] for i in dp])
print(ans1, ans2)
