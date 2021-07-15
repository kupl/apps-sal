"""
Codeforces Round #335 (Div. 2)
Problem 606 B. Testing Robots

@author yamaton
@date 2015-12-11
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(x, y, x0, y0, s):
    dir = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
    seen = set()
    pos = (x0, y0)
    result = []

    for c in s:
        if pos in seen:
            result.append(0)
        else:
            result.append(1)
            seen.add(tuple(pos))
        dx, dy = dir[c]
        (nx, ny) = (pos[0] + dx, pos[1] + dy)
        pos0 = nx if 1 <= nx <= x else pos[0]
        pos1 = ny if 1 <= ny <= y else pos[1]
        pos = (pos0, pos1)
        # pp(pos)

    result.append(x * y - len(seen))
    return result


def pp(*args, **kwargs):
    return print(*args, file=sys.stderr, **kwargs)


def main():
    x, y, x0, y0 = map(int, input().split())
    s =  input().strip()
    result = solve(x, y, x0, y0, s)
    print(*result)


def __starting_point():
    main()

__starting_point()
