import sys
import heapq
import functools
import collections
import math
import random
from collections import Counter, defaultdict


def solve(lst):
    lst = sorted(lst)
    console('----- solving ------')
    console(lst)
    if len(lst) > 40:
        return sum(lst) - len(lst)
    base = 0
    minres = 10 ** 11
    while base ** len(lst) < 10 ** 15:
        req = [base ** i for i in range(len(lst))]
        diff = [abs(r - x) for (r, x) in zip(req, lst)]
        minres = min(minres, sum(diff))
        base += 1
    return minres


def console(*args):
    print('\x1b[36m', *args, '\x1b[0m', file=sys.stderr)
    return


for _ in range(1):
    _ = int(input())
    lst = list(map(int, input().split()))
    res = solve(lst)
    print(res)
