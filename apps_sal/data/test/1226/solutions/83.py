mod = 10 ** 9 + 7
(n, a, b) = map(int, input().split())


def combination(n, a):
    res = 1
    div = 1
    for i in range(a):
        res *= n - i
        res %= mod
        div *= a - i
        div %= mod
    res = res * pow(div, mod - 2, mod) % mod
    return res


print((pow(2, n, mod) - 1 - combination(n, a) - combination(n, b)) % mod)
