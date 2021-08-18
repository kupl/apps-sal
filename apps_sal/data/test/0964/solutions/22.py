"""
Codeforces Round 

Problem 581 D. Three Logos

@author yamaton
@date 2015-10-06
"""

import itertools as it
import functools
import operator
import collections
import math
import sys
import bisect


def solve(x1, y1, x2, y2, x3, y3):
    x1, y1 = min(x1, y1), max(x1, y1)
    x2, y2 = min(x2, y2), max(x2, y2)
    x3, y3 = min(x3, y3), max(x3, y3)
    pairs = [(x1, y1), (x2, y2), (x3, y3)]

    area = sum(x * y for (x, y) in pairs)
    side = math.floor(math.sqrt(area))
    if side * side != area:
        return None

    count = [y1, y2, y3].count(side)

    if count == 3:
        if x1 + x2 + x3 == side:
            As = 'A' * side
            Bs = 'B' * side
            Cs = 'C' * side
            return ([As for _ in range(x1)]
                  + [Bs for _ in range(x2)]
                  + [Cs for _ in range(x3)])

    result = []
    abc = 'ABC'
    if count == 1:
        i, x, y = next((i, x, y) for i, (x, y) in enumerate(pairs) if y == side)
        result.append((abc[i], (x, y)))

        length = side - x
        tmp = 0
        for k, (x, y) in enumerate(pairs):
            if k == i:
                continue
            if x == length:
                tmp += y
                result.append((abc[k], (x, y)))
            elif y == length:
                tmp += x
                result.append((abc[k], (y, x)))
            else:
                return None

        if tmp == side:
            c, (x0, y0) = result[0]
            c1, (x1, y1) = result[1]
            c2, (x2, y2) = result[2]

            top = [c * side for _ in range(x0)]
            bottom = [c1 * y1 + c2 * y2 for _ in range(x1)]
            return top + bottom

    return None


def main():
    xys = [int(i) for i in input().strip().split()]
    assert len(xys) == 6
    result = solve(*xys)

    if result is None:
        print(-1)
    else:
        print(len(result))
        for line in result:
            print(line)


def __starting_point():
    main()


__starting_point()
