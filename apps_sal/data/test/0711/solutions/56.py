from collections import defaultdict

def prime_factors(n):
    d = defaultdict(int)
    while n%2 == 0:
        d[2] += 1
        n //= 2
    i = 3
    while i*i <= n:
        while n%i == 0:
            d[i] += 1
            n //= i
        i += 2
    if n > 2:
        d[n] += 1
    return d

# Combination
MOD = 10**9+7
MAX = 2*10**5
fac = [1,1] + [0]*MAX
finv = [1,1] + [0]*MAX
inv = [0,1] + [0]*MAX
for i in range(2,MAX+2):
    fac[i] = fac[i-1] * i % MOD
    inv[i] = -inv[MOD%i] * (MOD // i) % MOD
    finv[i] = finv[i-1] * inv[i] % MOD

def comb(n,r):
    if n < r: return 0
    if n < 0 or r < 0: return 0
    return fac[n] * (finv[r] * finv[n-r] % MOD) % MOD

N, M = list(map(int, input().split()))
ans = 1
pf = prime_factors(M)
for k,v in list(pf.items()):
    ans *= comb(v+N-1, N-1)
    ans %= MOD
print(ans)

