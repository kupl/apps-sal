N = int(input())
s1 = list(input())
s2 = list(input())
dp = [0] * N
if s1[0] == s2[0]:
    dp[0] = 3
else:
    dp[0] = 6
for i in range(1, N):
    if s1[i] == s2[i]:
        if s1[i - 1] == s2[i - 1]:
            dp[i] = 2 * dp[i - 1] % (10 ** 9 + 7)
        else:
            dp[i] = dp[i - 1]
    elif s1[i] == s1[i - 1]:
        dp[i] = dp[i - 1]
    elif s1[i - 1] != s2[i - 1]:
        dp[i] = 3 * dp[i - 1] % (10 ** 9 + 7)
    else:
        dp[i] = 2 * dp[i - 1] % (10 ** 9 + 7)
print(dp[N - 1])
