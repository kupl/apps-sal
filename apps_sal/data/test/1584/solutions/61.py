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
        for j in range(i+1, n):
            k = bisect.bisect_left(l, l[i]+l[j])
            res += max(k-(j+1), 0)
    print(res)
    return 0

def __starting_point():
    solve()
__starting_point()
