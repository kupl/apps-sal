#!/usr/local/bin/python3.3 -tt

import fractions
import sys


def __starting_point():
    def _(f):
        for l in f:
            for i in l.split():
                yield int(i)

    g = _(sys.stdin)

    pq = fractions.Fraction(next(g), next(g))

    n, a = next(g), []

    for i in range(n):
        a.append(next(g))

    r = fractions.Fraction(a.pop())

    while a:
        r = fractions.Fraction(a.pop()) + fractions.Fraction(1, r)

    if r == pq:
        print("YES")
    else:
        print("NO")

__starting_point()
