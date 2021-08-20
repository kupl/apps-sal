import collections
import itertools
import functools
import math
import fractions
import operator


def lcm(a, b):
    return a * b // fractions.gcd(a, b)


def solve(n):
    if n <= 2:
        return n
    if n % 2 == 1:
        return lcm(n, lcm(n - 1, n - 2))
    offset = 100
    if n - offset < 0:
        offset = n
    r = 1
    for i in range(n, n - offset, -1):
        for j in range(i, n - offset, -1):
            for k in range(j, n - offset, -1):
                r = max(r, lcm(i, lcm(j, k)))
    return r


def __starting_point():
    print(solve(int(input())))


__starting_point()
