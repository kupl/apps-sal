s = input()
mod = 10 ** 9 + 7

l = len(s)
dp = [[0] * 4 for _ in range(l + 1)]
dp[0][0] = 1

for i, e in enumerate(s, 1):
    # do not use in ABC
    for j in range(4):
        if e == "?":
            dp[i][j] += dp[i - 1][j] * 3
        else:
            dp[i][j] += dp[i - 1][j]

    # use in ABC
    if e == "A" or e == "?":
        dp[i][1] += dp[i - 1][0]
    if e == "B" or e == "?":
        dp[i][2] += dp[i - 1][1]
    if e == "C" or e == "?":
        dp[i][3] += dp[i - 1][2]

    for j in range(4):
        dp[i][j] %= mod


ans = dp[l][3]
print(ans)
