from collections import defaultdict


def comb(n, k, mod=10 ** 9 + 7):
    denominator = 1
    numerator = 1
    for i in range(1, k + 1):
        denominator = denominator * i % mod
    for i in range(n - k + 1, n + 1):
        numerator = numerator * i % mod
    return numerator * pow(denominator, mod - 2, mod) % mod


def main():
    n, m = list(map(int, input().split()))
    factorization = defaultdict(int)
    while not m % 2:
        factorization[2] += 1
        m //= 2
    f = 3
    while f * f <= m:
        if not m % f:
            factorization[f] += 1
            m //= f
        else:
            f += 2
    if m != 1:
        factorization[m] += 1
    ans = 1
    mod = 10 ** 9 + 7
    for _, c in list(factorization.items()):
        ans *= comb(c + n - 1, c, mod)
        ans %= mod
    print(ans)


def __starting_point():
    main()


__starting_point()
