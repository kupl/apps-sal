n, a, b = list(map(int, input().split()))
mod = 10 ** 9 + 7


def inv(x):
    return pow(x, mod - 2, mod)


def c(n, k):
    ue, sita = 1, 1
    for i in range(0, k):
        ue = ue * (n - i) % mod
        sita = sita * (i + 1) % mod
    return ue * inv(sita) % mod


print((((pow(2, n, mod) - c(n, a) - c(n, b) - 1) % mod + mod) % mod))
