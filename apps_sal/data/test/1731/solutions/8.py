n_=2*10**3
mod=10**9+7
fac=[1]*(n_+1)
for i in range(1,n_+1):
    fac[i]=fac[i-1]*i%mod
inv =[1]*(n_+1)
inv[n_]=pow(fac[n_],mod-2,mod)
for i in range(n_-1,0,-1):
    inv[i]=inv[i+1]*(i+1)%mod
def nCr(n,r):
    if n<=0 or r<0 or r>n:
        return 0
    return fac[n]*inv[r]%mod*inv[n-r]%mod

n,m=map(int,input().split())
ans=nCr(n+2*m-1,n-1)
print(ans)
