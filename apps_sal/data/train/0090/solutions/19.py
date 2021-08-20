import sys
import heapq
import functools
import collections
import math
import random
from collections import Counter, defaultdict


def solve(arr, brr):
    console('----- solving ------')
    movable = []
    for (a, b) in zip(arr, brr):
        if b == 0:
            movable.append(a)
    movable = sorted(movable)
    for i in range(len(arr)):
        if brr[i] == 0:
            arr[i] = movable.pop()
    return arr


def console(*args):
    print('\x1b[36m', *args, '\x1b[0m', file=sys.stderr)
    return


for case_num in range(int(input())):
    k = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    res = solve(arr, brr)
    print(' '.join([str(x) for x in res]))
