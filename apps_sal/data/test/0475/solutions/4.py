import math


def modi(a, m):
    return pow(a, m - 2, m)


def __starting_point():
    (n, m, k) = [int(x) for x in input().split()]
    mod = 998244353
    ans = 1
    for i in range(k):
        ans *= (n - 1 - i) % mod
        ans = ans % mod
    for i in range(1, k + 1):
        ans *= modi(i, mod) % mod
        ans = ans % mod
    ans *= m
    ans = ans % mod
    ans *= pow(m - 1, k, mod) % mod
    ans = ans % mod
    print(ans)


__starting_point()
