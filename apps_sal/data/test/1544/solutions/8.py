from math import factorial


def C(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)


def main():
    n = int(input())
    print(C(n + 4, 5) * C(n + 2, 3))


def __starting_point():
    main()


__starting_point()
