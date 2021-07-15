def comb(n, r, p):
    num, den = 1, 1
    r = min(r, n - r)
    for i in range(1, r + 1):
        num = num * (n - i + 1) % p
        den = den * i % p
    return num * pow(den, p - 2, p) % p


n, a, b = list(map(int, input().split()))
MOD = 1_000_000_007
ans = pow(2, n, MOD)
ans %= MOD
ans -= comb(n, a, MOD)
ans %= MOD
ans -= comb(n, b, MOD)
ans %= MOD
ans -= 1
ans %= MOD
print(ans)

