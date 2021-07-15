import sys
pin=sys.stdin.readline
sys.setrecursionlimit(10000000)

def f(n):
  if n==0:
    return 1
  if n==1:
    if dp[n]==0:
      return 0
    return 1
  if dp[n]==0:
    return 0
  if dp[n-1]==-1:
    dp[n-1]=f(n-1)
  if dp[n-2]==-1:
    dp[n-2]=f(n-2)
  return dp[n-1]+dp[n-2]


N,M=map(int,pin().split())
mod=1000000007
dp=[-1]*(N+1)
dp[0]=1
for i in range(M):
  dp[int(pin())]=0
print(f(N)%mod)
