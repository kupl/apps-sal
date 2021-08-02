N, M = map(int, input().split())

mod = 10 ** 9 + 7
#L = 5 * 10**5
fac = [1, 1]
finv = [1, 1]
inv = [0, 1]


def comb(n, r):
    return fac[n] * (finv[r] * finv[n - r] % mod) % mod


def perm(n, r):
    return fac[n] * finv[n - r] % mod


for i in range(2, M + 1):
    fac.append((fac[-1] * i) % mod)
    inv.append(mod - (inv[mod % i] * (mod // i) % mod))
    finv.append(finv[-1] * inv[-1] % mod)

ans = 0

for K in range(N + 1):
    ans += comb(N, K) * (-1)**(K % 2) % mod * perm(M, K) % mod * pow(perm(M - K, N - K), 2, mod)
    ans %= mod

print(ans)
