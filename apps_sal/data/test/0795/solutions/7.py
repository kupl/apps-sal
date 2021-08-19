from math import sqrt
from fractions import gcd


def main():
    (limit, res) = (int(input()), 0)
    for m in range(2, int(sqrt(limit)) + 1):
        mm = m * m
        for n in range(1 + (m & 1), m, 2):
            nn = n * n
            c = mm + nn
            if c > limit:
                break
            if gcd(mm - nn, c) == 1:
                res += limit // c
    print(res)


def __starting_point():
    main()


__starting_point()
