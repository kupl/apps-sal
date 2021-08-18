def prepare(n, mod):
    fac = [1]
    for i in range(1, n + 1):
        fac.append((fac[-1] * i) % mod)

    rec = pow(fac[-1], mod - 2, mod)

    den = [1 for _ in range(n + 1)]
    den[n] = rec
    for i in range(n - 1, 0, -1):
        rec = (rec * (i + 1)) % mod
        den[i] = rec

    return fac, den


def comb_mod(n, r, mod, fac, den):
    return (fac[n] * den[r] * den[n - r]) % mod


r1, c1, r2, c2 = map(int, input().split())

mod = 10**9 + 7
fac, den = prepare(r2 + c2 + 2, mod)

ans = comb_mod(r2 + 1 + c2 + 1, c2 + 1, mod, fac, den)
ans -= comb_mod(r2 + 1 + c1, c1, mod, fac, den)
ans -= comb_mod(r1 + c2 + 1, c2 + 1, mod, fac, den)
ans += comb_mod(r1 + c1, c1, mod, fac, den)

print(ans % mod)
