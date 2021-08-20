MOD = 10 ** 9 + 7
(n, m, k) = list(map(int, input().split()))


def f(i, j):
    return i * (i - 1) * (i + 1) // 6 * j ** 2


def c(a, b):
    r = 1
    for i in range(a, a - b, -1):
        r = r * i % MOD
    t = 1
    for i in range(1, b + 1):
        t = t * i % MOD
    return r * pow(t, MOD - 2, MOD)


print((f(n, m) + f(m, n)) * c(n * m - 2, k - 2) % MOD)
