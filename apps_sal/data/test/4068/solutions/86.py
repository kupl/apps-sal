n,m=map(int,input().split())
a=[int(input()) for i in range(m)]
mod=10**9+7
ans=1

dp=[0]*(n+1)
dp[0]=1
dp[1]=1
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]
    dp[i]%=mod
if m==0:
    ans=dp[n]
else:
    begin=0
    end=a[0]-1
    for i in range(m):
        end=a[i]-1
        ans*=dp[end-begin]
        
        if(i+1<m and a[i+1]==a[i]+1):
            ans=0
            break
            
        else:
            begin=end+2

    ans*=dp[n-a[m-1]-1]

print(ans%mod)
