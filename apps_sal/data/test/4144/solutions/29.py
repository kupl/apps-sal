def pow(a, x):
    if x == 0:
        return 1
    else:
        y, r = divmod(x, 2)
        sq = pow(a, y)
        if r == 1:
            return (sq * sq * a) % (10 ** 9 + 7)
        else:
            return (sq * sq) % (10 ** 9 + 7)


def __starting_point():
    n = int(input())
    print((pow(10, n) - 2 * pow(9, n) + pow(8, n)) % (10 ** 9 + 7))


__starting_point()
