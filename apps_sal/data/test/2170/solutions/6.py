n, m = map(int, input().split())
mod = 10**9 + 7


def cmb(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod


N = 10**6
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)

"""
1つ当たっている→Freeはn-1個→m-1 C n-1
同様に2つ→m-2 C n-2
数は？→ n C 2
包除原理
"""
mode = -1
ans = 0
for i in range(n + 1):
    mode = -mode
    ans = (ans + mode * cmb(n, i, mod) * cmb(m - i, n - i, mod) * fact[n - i]) % mod
print(ans * cmb(m, n, mod) * fact[n] % mod)
