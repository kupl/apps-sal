(x, y) = map(int, input().split())
mod = 10 ** 9 + 7
a = (2 * x - y) // 3
b = (2 * y - x) // 3
if a != (2 * x - y) / 3 or b != (2 * y - x) / 3:
    print(0)
elif a < 0 or b < 0:
    print(0)
else:
    max = a + b + 10
    fac = [0] * max
    finv = [0] * max
    inv = [0] * max
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, max):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod
    ans = fac[a + b] * (finv[a] * finv[b] % mod) % mod
    print(ans)
