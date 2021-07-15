def main():
    n, m = list(map(int, input().split()))
    if n > m * 2:
        n = m * 2
    elif m > n * 2:
        m = n * 2
    print((n + m) // 3)


def __starting_point():
    main()

__starting_point()
