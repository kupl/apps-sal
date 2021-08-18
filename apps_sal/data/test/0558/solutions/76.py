N, M, K = list(map(int, input().split()))
mod = 998244353


def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


p = 998244353
N1 = 2 * 10 ** 5 + 10
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N1 + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

ans = 0
mem = 1
mem = pow(M - 1, N - K - 1, p)
for i in range(K, -1, -1):
    wk = M * mem
    wk %= p
    wk *= cmb(N - 1, i, p)
    mem *= (M - 1)
    mem %= p
    ans += wk
    ans %= p

print(ans)
