"""
Codeforces Round #332 (Div. 2)

Problem 599 D. Spongebob and Squares

@author yamaton
@date 2015-11-20
"""
import itertools as it
import functools
import operator
import collections
import math
import sys


def solve(x):

    def find_p(n):
        return (6 * x // (n * (n + 1)) - 2 * n - 1) // 3

    def f(n, p):
        return n * (n + 1) * (2 * n + 3 * p + 1) - 6 * x
    result = []
    for n in it.count(1):
        p = find_p(n)
        if p < 0:
            break
        if f(n, p) == 0:
            result.append((n, n + p))
            if p > 0:
                result.append((n + p, n))
    result.sort()
    return result


def main():
    x = int(input())
    results = solve(x)
    print(len(results))
    for res in results:
        print(*res)


def __starting_point():
    main()


__starting_point()
