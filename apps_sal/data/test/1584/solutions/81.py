import math
import collections
import fractions
import itertools
import functools
import operator
import bisect


def solve():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    res = 0
    for i in range(n):
        k = i
        for j in range(i + 1, n):
            while k < n and l[k] < l[i] + l[j]:
                k += 1
            res += k - (j + 1)
    print(res)
    return 0


def __starting_point():
    solve()


__starting_point()
