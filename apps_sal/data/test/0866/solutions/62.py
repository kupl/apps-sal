def COMinit():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, max):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod


def COM(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod


mod = 10 ** 9 + 7
(X, Y) = list(map(int, input().split()))
a = X % 2
b = X // 2
for i in range(b + 1):
    if a * 2 + b * 1 == Y:
        break
    a += 2
    b -= 1
if a * 2 + b * 1 != Y:
    print(0)
else:
    max = a + b + 1
    fac = [0] * max
    finv = [0] * max
    inv = [0] * max
    COMinit()
    print(COM(a + b, a))
