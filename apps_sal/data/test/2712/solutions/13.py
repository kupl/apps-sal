import sys
import heapq
import functools
import collections
import math
import random
from collections import Counter, defaultdict


def solve(a, b, c):
    console('----- solving ------')
    return max([a, b, c])


def console(*args):
    print('\x1b[36m', *args, '\x1b[0m', file=sys.stderr)
    return


for case_num in range(int(input())):
    (a, b, c) = list(map(int, input().split()))
    res = solve(a, b, c)
    print(res)
