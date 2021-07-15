S = int(input())
mod = 10**9 + 7

dp = [0] * (S+1)
dp[0] = 1
x = 0
for i in range(1,S+1,1):
  if i >= 3:
    x += dp[i-3] % mod
  dp[i] = x % mod

ans = dp[S] % mod
print(ans)
