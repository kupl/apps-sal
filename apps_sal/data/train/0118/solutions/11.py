import sys
import heapq
import functools
import collections
import math
import random
from collections import Counter, defaultdict


def solve(lst, x):
    console("----- solving ------")

    lst = sorted(lst)[::-1]

    cnt = 0
    pdt = lst[0]
    res = 0
    for i in lst:
        cnt += 1
        pdt = min(i, pdt)
        if cnt * pdt >= x:
            res += 1
            cnt = 0
            pdt = i

    return res


def console(*args):
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return


for case_num in range(int(input())):

    _, x = list(map(int, input().split()))
    lst = list(map(int, input().split()))

    res = solve(lst, x)

    print(res)
