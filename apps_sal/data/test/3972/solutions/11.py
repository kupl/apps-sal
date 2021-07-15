n = int(input())
if n <= 3:
  print([n,n**2,n*(2*n-1)][n-1])
  return
mod = 10**9+7
dp = [0]*(n+1)
dp[1] = n
dp[2] = n**2
dp[3] = n*(2*n-1)
acc = sum(dp)
for i in range(4,n+1):
  dp[i] = acc-dp[i-2]+(n-1)**2+n-i+2
  dp[i] %= mod
  acc = (acc+dp[i])%mod
print(dp[n])
