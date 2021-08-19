def combination(n, r, mod=10 ** 9 + 7):
    (n1, r) = (n + 1, min(r, n - r))
    numer = denom = 1
    for i in range(1, r + 1):
        numer = numer * (n1 - i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod - 2, mod) % mod


mod = 10 ** 9 + 7
(r1, c1, r2, c2) = list(map(int, input().split()))
r2 += 1
c2 += 1
a1 = combination(r1 + c1, r1)
a2 = combination(r2 + c2, r2)
a3 = combination(r1 + c2, r1)
a4 = combination(r2 + c1, r2)
print((a1 + a2 - a3 - a4) % mod)
