n, m = map(int, input().split())
a_l = [int(input()) for _ in range(m)]

dp = [1] * (n + 1)
dp[0] = 1
if 1 not in a_l:
    dp[1] = 1
else:
    dp[1] = 0
if n > 1:
    for i in a_l:
        dp[i] = 0
    if 2 not in a_l:
        dp[2] = dp[0] + dp[1]
    else:
        dp[2] = 0
    for i in range(2, n + 1):
        if dp[i] != 0:
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
print(dp[-1])
