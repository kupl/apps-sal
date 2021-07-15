n=int(input())
c=list(map(int,input().split()))
mod=10**9+7
c.sort(reverse=True)
ans=0
po2=[1]
for i in range(n):
    po2.append(po2[-1]*2%mod)
for i,j in enumerate(c,1):
    ans+=j*((i-1)*po2[i-2]+po2[i-1])*po2[n-i]*po2[n-i]*po2[i]%mod
    ans%=mod
print(ans)
