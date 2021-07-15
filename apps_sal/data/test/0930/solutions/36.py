# comb_mod(n, c, r, mod, fac, den) ≡ nCr
def prepare(n, mod):
    # fac[i] ≡ i!
    fac = [1]
    for i in range(1, n+1):
        fac.append((fac[-1] * i) % mod)

    # rec ≡ 1 / n!
    rec = pow(fac[-1], mod-2, mod)

    # den[i] ≡ 1 / i!
    den = [1 for _ in range(n+1)]
    den[n] = rec
    for i in range(n-1, 0, -1):
        rec = (rec * (i+1)) % mod
        den[i] = rec
    
    return fac, den

def comb_mod(n, r, mod, fac, den):
    return (fac[n] * den[r] * den[n - r]) % mod

n, k = map(int, input().split())
mod = 10**9 + 7
fac, den = prepare(2*n-1, mod)

if k >= n-1:
    print(comb_mod(2*n-1, n, mod, fac, den))
else:
    ans = 0
    for i in range(k+1):
        ans += comb_mod(n-1, i, mod, fac, den) * comb_mod(n, i, mod, fac, den)
        ans %= mod
    print(ans)
