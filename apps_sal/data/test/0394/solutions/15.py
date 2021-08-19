import sys
import math


def period(x):
    n = len(x)
    res = []
    for i in range(1, len(x)):
        if all((i == j for (i, j) in zip(x, x[i:]))):
            res.append(i)
    return res + [n]


def main():
    [n] = map(int, next(sys.stdin).split())
    a = list(map(int, next(sys.stdin).split()))
    a = [0] + a
    x = [j - i for (i, j) in zip(a, a[1:])]
    periods = period(x)
    print(len(periods))
    print(' '.join(map(str, periods)))


def __starting_point():
    main()


__starting_point()
