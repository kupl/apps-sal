3


def readln():
    return list(map(int, input().split()))


def main():
    (n, k) = readln()
    if k >= n // 2:
        print((n - 1) * n // 2)
    else:
        k = n - 2 * k
        print((n - 1) * n // 2 - k * (k - 1) // 2)


def __starting_point():
    main()


__starting_point()
