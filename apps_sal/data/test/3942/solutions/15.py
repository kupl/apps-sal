import collections
import itertools
import functools
import math


def valid(s, r):
    r = iter(r)
    op = 0
    cl = 0
    for c in s:
        if c == '(':
            op += 1
        elif c == ')':
            cl += 1
        elif c == '
            cl += next(r)
        if cl > op:
            return False
    return True


def solve(s):
    FAIL = [-1]
    op = s.count('(')
    cl = s.count(')')
    h = s.count('

    if cl + h > op:
        return FAIL

    r=[1] * h
    r[-1] += (op - cl - h)

    if not valid(s, r):
        return FAIL
    return r


def __starting_point():
    for n in solve(input()):
        print(n)


__starting_point()
