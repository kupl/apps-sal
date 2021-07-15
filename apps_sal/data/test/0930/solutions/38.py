n,k=map(int,input().split())
mod=10**9+7

MAX_N=10**6
fact=[1]
fact_inv=[0]*(MAX_N+4)
for i in range(MAX_N+3):
  fact.append(fact[-1]*(i+1)%mod)

fact_inv[-1]=pow(fact[-1],mod-2,mod)
for i in range(MAX_N+2,-1,-1):
  fact_inv[i]=fact_inv[i+1]*(i+1)%mod

def f(n,k,mod):
  return fact[n]*fact_inv[k]%mod*fact_inv[n-k] %mod

ans=0
#0人の部屋はmaxいくつできるか
a=min(k,n-1)
ans=0
for i in range(a+1):
  d=f(n,i,mod)*f(n-1,i,mod)
  #print(i,d)
  ans+=d%mod
  ans%=mod

print(ans)
