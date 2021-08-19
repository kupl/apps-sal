def main():
    from math import factorial

    def calc(x):
        ret = 1
        for i in range(x):
            ret = ret * (n - i) % mod
        return ret * pow(factorial(x), mod - 2, mod) % mod
    (n, a, b) = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    print(max(0, (pow(2, n, mod) - (calc(a) + calc(b)) % mod - 1) % mod))


def __starting_point():
    main()


__starting_point()
