n, a, b = list(map(int, input().split()))
# 全通り - nCa - nCb
mod = 10 ** 9 + 7


def inv(x):
    return pow(x, mod - 2, mod)

# n ~ n - k + 1


def c(n, k):
    res = 1
    for i in range(0, k):
        res = res * (n - i) * inv(i + 1) % mod
    return res


print((((pow(2, n, mod) - c(n, a) - c(n, b) - 1) % mod + mod) % mod))
