n = int(input())
s = input()
n = len(s)
dp = [[0, 0, 0] for _ in range(n)]

if s[0] == "C":
    dp[0][0] = 1
if s[0] == "M":
    dp[0][1] = 1
if s[0] == "Y":
    dp[0][2] = 1
if s[0] == "?":
    dp[0][0] = 1
    dp[0][1] = 1
    dp[0][2] = 1

for i, c in enumerate(s[1:]):
    if c == "C":
        dp[i + 1][0] += dp[i][1] + dp[i][2]
    if c == "M":
        dp[i + 1][1] += dp[i][0] + dp[i][2]
    if c == "Y":
        dp[i + 1][2] += dp[i][0] + dp[i][1]
    if c == "?":
        dp[i + 1][0] += dp[i][1] + dp[i][2]
        dp[i + 1][1] += dp[i][0] + dp[i][2]
        dp[i + 1][2] += dp[i][0] + dp[i][1]

if sum(dp[-1]) > 1:
    print('Yes')
else:
    print('No')
