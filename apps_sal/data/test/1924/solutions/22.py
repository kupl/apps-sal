MOD = 10**9+7

# フェルマーの小定理
def nCr(n, r, mod=MOD):
    r = min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n+1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod

def g(r, c):
    return nCr(r+c+2, r+1) - 1

r1, c1, r2, c2 = list(map(int, input().split()))
r1 -= 1; c1 -= 1
ans = g(r2, c2)
ans -= g(r1, c2)
ans -= g(r2, c1)
ans += g(r1, c1)
ans += MOD * 2
ans %= MOD
print(ans)

