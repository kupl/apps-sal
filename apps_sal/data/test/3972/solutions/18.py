n=int(input())
mod=10**9+7

dp=[0 for i in range(0,10**6+1)]
S=[0 for i in range(0,10**6+1)]

dp[1]=1
dp[2]=1
S[1]=1
S[2]=2
for i in range(3,10**6+1):
    dp[i]=(S[i-1]-dp[i-2]+1)%mod
    S[i]=(S[i-1]+dp[i])%mod

if n==1:
    print(1)
elif n==2:
    print(4)
else:
    ans=(S[n-2]*(n-1)**2+(n-1)**2+(n-1)*S[n-1]+n)%mod
    print(ans)
