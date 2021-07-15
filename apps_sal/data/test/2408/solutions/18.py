#!/usr/local/bin/python3.5 -tt

import random
import sys

from fractions import Fraction, gcd

INF = 10 ** 9

def __starting_point():
    def _(f):
        for l in f:
            for i in l.split():
                yield int(i)

    g = _(sys.stdin)

    n = next(g)

    pts = []

    for i in range(n):
        x, y = (next(g),
                next(g),
                )

        pts.append((x, y))

    lines = set()
        
    for i in range(n):
        for j in range(i + 1, n):
            x0, y0, x1, y1 = (pts[i][0],
                              pts[i][1],
                              pts[j][0],
                              pts[j][1],
                              )
                              
            dx, dy = (x1 - x0,
                      y1 - y0,
                      )

            g = gcd(dx, dy)

            dx //= g
            dy //= g

            if dx:
                a = Fraction(dy, dx)

                b = - Fraction(dy * x0, dx) + y0
            else:
                a, b = (INF,
                        x0,
                        )

            lines.add((a, b))

    a = list(lines)

    size = len(lines)
    
    c = 0

    for i in range(size):
        for j in range(i + 1, size):
            if a[i][0] == a[j][0]:
                continue

            c += 1

    print(c)

__starting_point()
