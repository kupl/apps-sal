n, k = list(map(int, input().split()))
a = [int(x) for x in input().split()]
a.sort()
MOD = 10**9 + 7


def cmb(n, r, p):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, n + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)

ans = 0
for i in range(0, n - k + 1):
    ans -= a[i] * cmb(n - i - 1, k - 1, MOD)
    ans += a[n - i - 1] * cmb(n - i - 1, k - 1, MOD)
    ans %= MOD
print(ans)
