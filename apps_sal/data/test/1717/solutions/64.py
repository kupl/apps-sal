def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    N = int(input())

    n = lcm(2, 3)
    for i in range(4, N + 1):
        if N == 2:
            print((3))
        elif N == 3:
            print((7))
        else:
            n = lcm(n, i)
    print((n + 1))


def __starting_point():
    main()


__starting_point()
