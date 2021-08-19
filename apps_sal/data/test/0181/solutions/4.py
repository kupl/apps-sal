def f(x):
    assert 0 <= x <= 360
    return min(x, 360 - x)


def main():
    x = int(input())
    (a, b, c, d) = (-x, -x + 90, -x + 180, -x + 270)
    (a, b, c, d) = (a % 360, b % 360, c % 360, d % 360)
    (a, b, c, d) = (f(a), f(b), f(c), f(d))
    L = [(a, 0), (b, 1), (c, 2), (d, 3)]
    L.sort()
    print(L[0][1])


def __starting_point():
    main()


__starting_point()
