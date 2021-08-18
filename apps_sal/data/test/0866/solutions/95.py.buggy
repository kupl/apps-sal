x, y = map(int, input().split())

mod = 10**9 + 7


def comb(n, r):
    if 2 * r > n:
        return comb(n, n - r)
    return fac[n] * inv[r] * inv[n - r] % mod


if (x + y) % 3 != 0:
    print(0)
    return

n = (x + y) // 3
x -= n
y -= n
if x < 0 or y < 0:
    print(0)
    return

fac = [1] * (n + 1)
inv = [1] * (n + 1)
for i in range(2, n + 1):
    fac[i] = fac[i - 1] * i % mod
inv[n] = pow(fac[n], mod - 2, mod)
for i in range(n - 1, 1, -1):
    inv[i] = inv[i + 1] * (i + 1) % mod

print(comb(x + y, x) % mod)
