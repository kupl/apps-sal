n, k = [int(item) for item in input().split()]
MOD = 10**9 + 7

MAX_N = 10**4

fac = [1] + [0] * MAX_N
fac_inv = [1] + [0] * MAX_N
for i in range(1, n + 1):
    fac[i] = fac[i - 1] * (i) % MOD
    # Fermat's little theorem says
    # a**(p-1) mod p == 1
    # then, a * a**(p-2) mod p == 1
    # it means a**(p-2) is inverse element
    fac_inv[i] = fac_inv[i - 1] * pow(i, MOD - 2, MOD) % MOD


def mod_nCr(n, r):
    if n == 0 and r == 0:
        return 1
    if n < r or n < 0:
        return 0
    tmp = fac_inv[n - r] * fac_inv[r] % MOD
    return tmp * fac[n] % MOD


ans = 0
total = pow(k, n * n, MOD)
for i in range(n + 1):
    for j in range(n + 1):
        not_one = (n - i + n - j) * n - ((n - i) * (n - j))
        free = n * n - not_one
        val = pow(-1, i + j) * mod_nCr(n, i) * mod_nCr(n, j) * pow(k - 1, not_one, MOD) * pow(k, free, MOD)
        ans += val
        ans %= MOD

print(ans)
