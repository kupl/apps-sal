n, k = list(map(int, input().split()))
mod = 1000000007
fac = [1]
inv = [1]
for i in range(n * 2):
    fac.append(fac[-1] * (i + 1) % mod)
    inv.append(pow(fac[-1], mod - 2, mod))


def cmb(n, k):
    if k < 0 or k > n:
        return 0
    return ((fac[n] * inv[k]) % mod * inv[n - k]) % mod


ret = 0
for m in range(min(k + 1, n)):
    ret = (ret + (cmb(n, m) * cmb(n - 1, n - m - 1)) % mod) % mod
print(ret)
