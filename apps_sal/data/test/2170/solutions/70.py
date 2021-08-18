SIZE = 5 * 10**5 + 1
MOD = 10**9 + 7

SIZE += 1
inv = [0] * SIZE
fac = [0] * SIZE
finv = [0] * SIZE
inv[1] = 1
fac[0] = fac[1] = 1
finv[0] = finv[1] = 1
for i in range(2, SIZE):
    inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD
    fac[i] = fac[i - 1] * i % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD


def choose(n, r):
    if 0 <= r <= n:
        return (fac[n] * finv[r] % MOD) * finv[n - r] % MOD
    else:
        return 0


def chofuku(n, r):
    return choose(n + r - 1, r)


def narabekae(n, r):
    return fac[n] * finv[n - r] % MOD


N, M = list(map(int, input().split()))
ans = 0
for k in range(N + 1):
    ans += choose(N, k) * narabekae(M - k, N - k) * (-1 if k % 2 == 1 else 1)
    ans %= MOD
ans *= narabekae(M, N)
print((ans % MOD))
