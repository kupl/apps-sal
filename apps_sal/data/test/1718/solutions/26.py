import math


def main():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    n = n - 1
    k = k - 1
    print((math.ceil(n / k)))


def __starting_point():
    main()


__starting_point()
