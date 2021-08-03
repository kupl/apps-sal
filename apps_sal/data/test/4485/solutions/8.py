import math
import collections
import fractions
import itertools
import functools
import operator
import bisect


def solve():
    n, m = map(int, input().split())
    course = [[] for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        course[a - 1].append(b)
        course[b - 1].append(a)
    for i in course[0]:
        if n in course[i - 1]:
            print("POSSIBLE")
            break
    else:
        print("IMPOSSIBLE")
    return 0


def __starting_point():
    solve()


__starting_point()
