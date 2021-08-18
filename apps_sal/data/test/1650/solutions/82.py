L = input()
p = 10**9 + 7
dp = [[0] * 2 for i in range(len(L) + 1)]
dp[0][0] = 1
for digit, i in enumerate(L):
    if L[digit] == "0":
        dp[digit + 1][0] = dp[digit][0]
        dp[digit + 1][1] = dp[digit][1]
    else:
        dp[digit + 1][1] = (dp[digit][0] + dp[digit][1]) % p
    if L[digit] == "0":
        dp[digit + 1][1] += dp[digit][1] * 2 % p
        dp[digit + 1][1] %= p
    else:
        dp[digit + 1][0] += dp[digit][0] * 2 % p
        dp[digit + 1][0] %= p
        dp[digit + 1][1] += dp[digit][1] * 2 % p
        dp[digit + 1][1] %= p
ans = (dp[len(L)][0] + dp[len(L)][1]) % p
print(ans)
