mod = 10 ** 9 + 7


def mod_prepare(N):
    fac = [1, 1]
    finv = [1, 1]
    inv = [0, 1]
    for i in range(2, N + 1):
        fac.append(fac[i - 1] * i % mod)
        inv.append(mod - inv[mod % i] * (mod // i) % mod)
        finv.append(finv[i - 1] * inv[i] % mod)
    return fac, finv


N, M = map(int, input().split())

fac, inv = mod_prepare(M)

ans = 0
sign = 1
for k in range(N + 1):
    ans += sign * fac[M - k] * inv[k] * inv[N - k]
    sign *= -1
    ans %= mod

print(ans * fac[N] * fac[M] * inv[M - N] * inv[M - N] % mod)
