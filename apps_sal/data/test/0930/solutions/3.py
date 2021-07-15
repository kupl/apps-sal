n,k = map(int,input().split())
mod = 1000000007
def comb(n,k):
    if n < k: return 0
    if n < 0 or k < 0: return 0
    return fac[n]*finv[k]%mod*finv[n-k]%mod
fac = [1]*(n+1)
finv = [1]*(n+1)
for i in range(1,n+1):
    fac[i] = fac[i-1]*i%mod
    finv[i] = pow(fac[i],mod-2,mod)

ans = 0
for i in range(min(k+1,n)):
    ans += comb(n,i)*comb(n-1,i)%mod
    ans %= mod
print(ans)
