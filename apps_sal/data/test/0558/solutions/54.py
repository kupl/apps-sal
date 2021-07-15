n,m,k=map(int,input().split())
mod=998244353
ma=[1]
for i in range(1,k+1):
    mad=ma[-1]*(n-i)*pow(i,mod-2,mod)
    ma.append(mad)
    ma[-1]%=mod
ans=0
for i in range(k+1):
    ans+=ma[i]*m*pow(m-1,n-i-1,mod)
    ans%=mod
print(ans)
