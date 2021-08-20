(n, k) = [int(item) for item in input().split()]
MOD = 10 ** 9 + 7
MAX_N = 10 ** 4
fac = [1] + [0] * MAX_N
fac_inv = [1] + [0] * MAX_N
for i in range(1, n + 1):
    fac[i] = fac[i - 1] * i % MOD
    fac_inv[i] = fac_inv[i - 1] * pow(i, MOD - 2, MOD) % MOD


def mod_nCr(n, r):
    if n == 0 and r == 0:
        return 1
    if n < r or n < 0:
        return 0
    tmp = fac_inv[n - r] * fac_inv[r] % MOD
    return tmp * fac[n] % MOD


ans = 0
for i in range(n + 1):
    base = pow(k, n - i, MOD) * pow(k - 1, i, MOD) - pow(k - 1, n, MOD) + MOD
    base % MOD
    val = pow(-1, i) * mod_nCr(n, i) * pow(base, n, MOD)
    ans += val
    ans %= MOD
print(ans)
