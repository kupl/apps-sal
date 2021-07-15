n, m, k = map(int, input().split())

mod = 1000000007
def pow(x, n):
    ret = 1
    while n > 0:
        if (n & 1) == 1:
            ret = (ret * x) % mod
        x = (x * x) % mod
        n >>= 1
    return ret

fac = [1]
inv = [1]
for i in range(1, n * m + 1):
    fac.append((fac[-1] * i) % mod)
    inv.append(pow(fac[i], mod - 2))

def cmb(n, k):
    return (fac[n] * inv[k] * inv[n - k]) % mod

def doit(n, m, k):
    ret = 0
    for d in range(m):
        ret = (ret + d * (m - d)) % mod
    return (ret * n * n * cmb(n * m - 2, k - 2)) % mod

print((doit(n, m, k) + doit(m, n, k)) % mod)
