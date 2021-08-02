
x, y = list(map(int, input().split()))

mod = pow(10, 9) + 7


def comint(n, mod):
    fac = [0 for _ in range(n)]
    finv = [0 for _ in range(n)]
    inv = [0 for _ in range(n)]
    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1

    for i in range(2, n):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod
    return fac, finv


def com(n, k, fac, finv, mod):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod


if (x + y) % 3 != 0:
    print((0))
else:
    n = (x + y) // 3
    a = x - n
    b = y - n
    fac, finv = comint(a + b + 1, mod)
    print((com(a + b, a, fac, finv, mod)))
