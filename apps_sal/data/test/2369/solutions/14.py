n,k=map(int,input().split())
a=sorted(list(map(int,input().split())))

mod=10**9+7
fac=[1]*n
finv=[1]*n
inv=[0]*n
inv[1]=1
for i in range(2,n):
  fac[i]=fac[i-1]*i%mod
  inv[i]=mod-inv[mod%i]*(mod//i)%mod
  finv[i]=finv[i-1]*inv[i]%mod
def comb(n,k):
  if n<k:
    return 0
  if n<0 or k<0:
    return 0
  return fac[n]*(finv[k]*finv[n-k]%mod)%mod

ans=0
for i in range(n-k+1):
  ans-=a[i]*comb(n-i-1,k-1)%mod
  ans%=mod
a=a[::-1]
for i in range(n-k+1):
  ans+=a[i]*comb(n-i-1,k-1)%mod
  ans%=mod
print(ans%mod)
