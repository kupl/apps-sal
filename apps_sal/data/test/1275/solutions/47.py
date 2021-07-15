n,k = map(int,input().split())
def g(t):
    if t<2 or 2*n<t:
        return 0
    if dp[t]>-1:
        return dp[t]
    if t-1<=n:
        dp[t]=t-1
        return dp[t]
    if t-1>n:
        dp[t]=2*n+1-t
        return dp[t]

dp = [-1]*(2*n+1)

ans = 0
for i in range(2,2*n+1):
    ans +=g(i)*g(i+k)
print(ans)
