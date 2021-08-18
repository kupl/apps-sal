import sys
import heapq
import functools
import collections
import math
import random
from collections import Counter, defaultdict


def solve(lst):
    console("----- solving ------")

    arr = []
    arr.extend(lst[::2])
    arr.extend(lst[1::2])
    arr.extend(lst[::2])
    arr.extend(lst[1::2])

    psum = []
    ps = 0
    for i in arr:
        ps += i
        psum.append(ps)

    res = 0
    sub_length = (len(lst) + 1) // 2
    for i in range(len(lst)):
        res = max(res, psum[i + sub_length] - psum[i])

    return res


def console(*args):
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return


_ = int(input())


lst = list(map(int, input().split()))


res = solve(lst)


print(res)
