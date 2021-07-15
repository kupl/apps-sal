n,m,k=map(int,input().split())
mod1,mod2=10**9+7,998244353
mod=mod2
MAX=n-1
fact=[1]*(MAX+1)
inv=[1]*(MAX+1)
for i in range(2,MAX+1):
    fact[i]=i*fact[i-1]%mod
inv[-1]=pow(fact[-1],mod-2,mod)
for i in range(MAX,1,-1):
    inv[i-1]=inv[i]*i%mod
def comb(x,y):return fact[x]*inv[y]%mod*inv[x-y]%mod if x>=y>=0 else 0
ans=0
cor=pow(m-1,n-1-k,mod)
for i in range(k,-1,-1):
    ans=(ans+comb(n-1,i)*cor)%mod
    cor=cor*(m-1)%mod

print(m*ans%mod)
