def mod_inverse(n, mod=10**9 + 7):
    return pow(n, mod - 2, mod)


def combination(n, k, mod=10**9 + 7):
    numer = denom = 1
    for i in range(k):
        numer = (numer * (n - i)) % mod
        denom = (denom * (i + 1)) % mod
    return (numer * mod_inverse(denom, mod)) % mod


mod = 10**9 + 7
r1, c1, r2, c2 = list(map(int, input().split()))
ans = combination(r1 + c1, r1) - combination(1 + r2 + c1, 1 + r2) - combination(1 + r1 + c2, r1) + combination(2 + r2 + c2, 1 + r2)
print((ans % mod))
