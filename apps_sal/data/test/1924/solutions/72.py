r1,c1,r2,c2 = map(int,input().split())

MOD = 10**9+7
MAXN = r2+c2+5
fac = [1,1] + [0]*MAXN
for i in range(2,MAXN+2):
    fac[i] = fac[i-1] * i % MOD

def inv(n):
    return pow(n,MOD-2,MOD)

def comb(n,r):
    if n < r: return 0
    if n < 0 or r < 0: return 0
    return fac[n] * inv(fac[r]) * inv(fac[n-r]) % MOD

ans = comb(r2+c2+2,r2+1) - comb(r2+c1+1,c1) - comb(r1+c2+1,r1) + comb(r1+c1,r1)
ans %= MOD
print(ans)
