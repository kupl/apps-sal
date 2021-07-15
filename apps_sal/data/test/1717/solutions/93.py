def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    N = int(input())
    y = 1

    for x in range(2, N + 1):
        y = lcm(y, x)

    print((y + 1))


def __starting_point():
    main()

__starting_point()
