"""
Codeforces Round 

Problem 577 B. Modulo Sum

@author yamaton
@date 2015-09-10
"""

import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(xs, m):
    modulos = set()
    for x in xs:
        modulos |= {(x + i) % m for i in modulos}
        modulos.add(x % m)
        if 0 in modulos:
            return True
    else:
        return False


def tf_to_yn(tf):
    return 'YES' if tf else 'NO'


def print_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    [n, m] = [int(i) for i in input().strip().split()]
    xs = [int(i) for i in input().strip().split()]
    assert len(xs) == n

    result = solve(xs, m)
    print(tf_to_yn(result))


def __starting_point():
    main()


__starting_point()
