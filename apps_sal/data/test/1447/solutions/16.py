def main():
    n, m = list(map(int, input().split()))
    if n == 1 == m:
        res = 1.
    else:
        res = (2 * n * m - n - m) / (n * m - 1) / n

    print('{:.16f}'.format(res))


def __starting_point():
    main()


__starting_point()
