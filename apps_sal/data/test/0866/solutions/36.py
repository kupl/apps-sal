(x, y) = map(int, input().split())
mod = 10 ** 9 + 7
a = (2 * y - x) / 3
b = (2 * x - y) / 3
if a < 0 or b < 0 or (2 * y - x) // 3 != a or ((2 * x - y) // 3 != b):
    print(0)
else:
    a = (2 * y - x) // 3
    b = (2 * x - y) // 3
    fac = [0] * (a + b + 1)
    finv = [0] * (a + b + 1)
    inv = [0] * (a + b + 1)
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, a + b + 1):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod
    print(fac[a + b] * (finv[a] * finv[b] % mod) % mod)
