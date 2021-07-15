n,m,k=map(int,input().split())
mod=998244353
cntb=1
ans=0
for i in range(k+1):
    ans=ans+(((m*pow(m-1,n-1-i,mod))%mod)*cntb)%mod
    ans=ans%mod
    cntb=(cntb*(n-1-i)*pow(i+1,mod-2,mod))%mod
print(ans%mod)
