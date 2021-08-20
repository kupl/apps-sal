def solve():

    def combis(n, k, mod):
        from math import factorial
        numerator = 1
        denominator = 1
        for i in range(k):
            numerator = numerator * (n - i) % mod
            denominator = denominator * (i + 1) % mod
        return numerator * pow(denominator, mod - 2, mod) % mod
    (n, a, b) = [int(i) for i in input().split()]
    mod = 10 ** 9 + 7
    ans = pow(2, n, mod) - 1 - combis(n, a, mod) - combis(n, b, mod)
    print(ans % mod)


def __starting_point():
    solve()


__starting_point()
