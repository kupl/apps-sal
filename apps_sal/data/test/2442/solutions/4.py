import sys
import heapq
import functools
import collections
import math
import random
from collections import Counter, defaultdict


def solve(lst):
    console("----- solving ------")

    c = Counter(lst)

    cur = 0
    while True:
        if c[cur] < 2:
            a = cur
            break
        cur += 1

    while True:
        if c[cur] < 1:
            b = cur
            break
        cur += 1

    return a + b


def console(*args):
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return


for case_num in range(int(input())):

    k = int(input())

    lst = list(map(int, input().split()))

    res = solve(lst)

    print(res)
