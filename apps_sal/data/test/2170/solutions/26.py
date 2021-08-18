N, M = map(int, input().split())
MOD = 10 ** 9 + 7

n = N + M
fac = [1] * (n + 1)
inv = [1] * (n + 1)
for j in range(1, n + 1):
    fac[j] = (fac[j - 1] * j) % MOD

inv[n] = pow(fac[n], MOD - 2, MOD)
for j in range(n - 1, -1, -1):
    inv[j] = (inv[j + 1] * (j + 1)) % MOD


def comb(n, r):
    if r > n or n < 0 or r < 0:
        return 0
    return (fac[n] * inv[n - r] * inv[r]) % MOD


def perm(n, r):
    if r > n or n < 0 or r < 0:
        return 0
    return comb(n, r) * fac[r] % MOD


ans = pow(perm(M, N), 2, MOD)
for r in range(1, N + 1):
    p = comb(M, r) * perm(N, r) * pow(perm(M - r, N - r), 2, MOD) % MOD
    p *= -(-1) ** (r % 2)
    ans -= p
    ans %= MOD

print(ans)
