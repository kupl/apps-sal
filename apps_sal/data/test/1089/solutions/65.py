n, m, k = map(int, input().split())

mod = 1000000007
fac = [1]
for i in range(1, n * m + 1):
    fac.append((fac[-1] * i) % mod)

def pow(x, n):
    ret = 1
    while n > 0:
        if (n & 1) == 1:
            ret = (ret * x) % mod
        x = (x * x) % mod
        n >>= 1
    return ret

def inv(i):
    return pow(fac[i], mod - 2)

def cmb(n, k):
    return (fac[n] * inv(k) * inv(n - k)) % mod

x = sum(d * (m - d) for d in range(m)) % mod
y = sum(d * (n - d) for d in range(n)) % mod

c = cmb(n * m - 2, k - 2)
x = (x * n * n * c) % mod
y = (y * m * m * c) % mod

print((x + y) % mod)
