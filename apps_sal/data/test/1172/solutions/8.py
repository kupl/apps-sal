s = input().rstrip()
dp = [0] * 4
dp[0] = 1
for i in range(len(s)):
    if s[i] == 'A':
        dp[1] += dp[0]
    elif s[i] == 'B':
        dp[2] += dp[1]
    elif s[i] == 'C':
        dp[3] += dp[2]
    else:
        dp = [dp[0] * 3, dp[1] * 3 + dp[0], dp[2] * 3 + dp[1], dp[3] * 3 + dp[2]]
    dp = list([x % (10 ** 9 + 7) for x in dp])
print(dp[3])
