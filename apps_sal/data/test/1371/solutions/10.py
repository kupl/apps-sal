# -*- coding utf-8 -*-

MOD = 10 ** 9 + 7

S = int(input())

if S < 3:
    print((0))
    return

dp = [1] * (S + 1)
dp[0] = 0
dp[1] = 0
dp[2] = 0

for i in range(3, S - 2):
    for j in range(i + 3, S + 1):
        dp[j] += dp[i]
        dp[j] %= MOD

ans = dp[S]

print(ans)

