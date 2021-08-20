import math


def modi(a, m):
    return pow(a, m - 2, m)


def __starting_point():
    (w, h) = [int(x) for x in input().split()]
    (u1, d1) = [int(x) for x in input().split()]
    (u2, d2) = [int(x) for x in input().split()]
    for i in range(h):
        w += h - i
        if h - i == d1:
            w -= u1
            w = max(0, w)
        if h - i == d2:
            w -= u2
            w = max(0, w)
    print(w)


__starting_point()
