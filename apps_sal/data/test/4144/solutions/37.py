

def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    mod = 10 ** 9 + 7

    ans = pow(10, n, mod)
    ans -= pow(9, n, mod)
    ans -= pow(9, n, mod)
    ans += pow(8, n, mod)

    print((ans % mod))


def __starting_point():
    main()


__starting_point()
