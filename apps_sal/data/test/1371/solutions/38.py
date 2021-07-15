S = int(input())
mod = 10 ** 9 + 7

dp = [0] * (S + 1)
dp[0] = 1

x = 0
for i in range(1,S+1):
    if i-3 >= 0:
        x += dp[i-3]
        x %= mod
    dp[i] = x

print(dp[S])
