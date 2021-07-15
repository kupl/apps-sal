#!/usr/bin/env python3

from collections import namedtuple
from functools   import reduce
from operator    import itemgetter

Point = namedtuple("Point", "x y d1 d2")

try:
    while True:
        n, x1, y1, x2, y2 = list(map(int, input().split()))
        points = [Point(x1, y1, 0, 1e18)]
        for i in range(n):
            x, y = list(map(int, input().split()))
            points.append(Point(x, y, (x - x1)**2 + (y - y1)**2, (x - x2)**2 + (y - y2)**2))
        result = 1e18
        l2 = itemgetter(3)
        result = reduce(
            min,
            list(map(
                lambda a: min(
                    result, a.d1 + reduce(max, list(map(l2, [p for p in points if p.d1 > a.d1])), 0)
                ),
                points,
            )),
        )
        print(result)

except EOFError:
    pass

