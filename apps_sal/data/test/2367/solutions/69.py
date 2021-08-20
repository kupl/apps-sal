MOD = 10 ** 9 + 7
(h, w, a, b) = map(int, input().split())
n = h + w
fac = [1] * (n + 1)
fac_inv = [0] * (n + 1)
for i in range(n):
    fac[i + 1] = fac[i] * (i + 1) % MOD
fac_inv[-1] = pow(fac[-1], MOD - 2, MOD)
for i in range(n, 0, -1):
    fac_inv[i - 1] = fac_inv[i] * i % MOD


def comb(n, k):
    if k < 0 or k > n:
        return 0
    x = fac[n] * (fac_inv[k] * fac_inv[n - k]) % MOD % MOD
    return x


ans = 0
for i in range(w - b):
    ans += comb(h - a - 1 + b + i, b + i) * comb(a - 1 + (w - b - i - 1), a - 1) % MOD
    ans %= MOD
print(ans)
