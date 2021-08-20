(N, M, K) = list(map(int, input().split()))
ans = 0


def cmb(n, r, p):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


p = 998244353
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
for i in range(2, N + 1):
    fact.append(fact[-1] * i % p)
    inv.append(-inv[p % i] * (p // i) % p)
    factinv.append(factinv[-1] * inv[-1] % p)
for i in range(K + 1):
    res_i = M * pow(M - 1, N - i - 1, p) % p
    res_i = res_i * cmb(N - 1, i, p) % p
    ans = (ans + res_i) % p
print(ans)
