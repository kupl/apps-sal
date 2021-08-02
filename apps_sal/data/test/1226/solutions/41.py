n, a, b = map(int, input().split())


def nCr(n, r):
    r = min(r, n - r)
    num, den = 1, 1
    for i in range(r):
        num = (num * (n - i)) % mod
        den = (den * pow(i + 1, mod - 2, mod)) % mod
    return num * den % mod


mod = 10**9 + 7
print((pow(2, n, mod) - nCr(n, a) - nCr(n, b) - 1) % mod)
