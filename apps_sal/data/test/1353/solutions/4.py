def main():
    n, m, a, b = list(map(int, input().split(' ')))
    c = 0
    if b / m < a:
        c += n // m * b
        n %= m
    else:
        c += n * a
        n = 0
    if n != 0:
        c += min(n * a, b)
    print(c)


def __starting_point():
    main()


__starting_point()
