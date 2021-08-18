n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()


def cmb(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod


mod = 10**9 + 7
N = 10**5 + 100
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)

maxans = 0
for i in range(k, n + 1):
    maxans = maxans + (a[i - 1] * (cmb(i, k, mod) - cmb(i - 1, k, mod))) % mod

minans = 0
for i in range(k, n + 1):
    minans = minans + (a[n - i] * (cmb(i, k, mod) - cmb(i - 1, k, mod))) % mod
print((maxans - minans) % mod)
