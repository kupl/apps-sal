MOD = 10**9 + 7
fac = [1,1] # 階乗 n!
inv = [0,1] # 逆元 1/n
finv = [1,1] # 逆元の階乗 (n^-1)! = (1/n)!

def finv_init(n, m):
    for i in range(2, n+1):
        fac.append( (fac[-1] * i ) % m )
        inv.append( (-inv[m%i] * (m//i)) % m )
        finv.append( (finv[-1] * inv[-1]) % m )

def nPr(n, r, m): return fac[n] * finv[n-r]

n, m = list(map(int, input().split()))
finv_init(m, MOD)
ans = 0
for d in range(0, n+1):
    a = nPr(m-d, n-d, MOD) * nPr(n, d, MOD) * finv[d] % MOD
    if d & 1: a = -a
    ans += a; ans %= MOD
ans *= nPr(m, n, MOD)
print((ans % MOD))

