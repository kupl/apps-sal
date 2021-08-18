

from functools import reduce
from operator import mul
from collections import Counter
from collections import deque
from itertools import accumulate
from queue import Queue
from queue import PriorityQueue as pq
from heapq import heapreplace
from heapq import heapify
from heapq import heappushpop
from heapq import heappop
from heapq import heappush
import heapq
import time
import random
import bisect
import itertools
import collections
from fractions import Fraction
import fractions
import string
import math
import operator
import functools
import copy
import array
import re
import sys
sys.setrecursionlimit(500000)


input = sys.stdin.readline


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    return


def warizan(a, b):
    return a // b, a % b


def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, list(range(n, n - r, -1)), 1)
    denom = reduce(mul, list(range(1, r + 1)), 1)
    return numer // denom


mod = 1000000007


def combinations_count_mod(n, r):
    r = min(r, n - r)
    numer = reduce(lambda x, y: x * y % mod, list(range(n, n - r, -1)), 1)
    denom = pow(reduce(lambda x, y: x * y % mod, list(range(1, r + 1)), 1), mod - 2, mod)
    return numer * denom % mod


a, b, x, y = list(map(int, input().strip().split()))
h = abs(a - b)
if a < b:
    temp1 = y * (h) + x
    temp2 = 2 * x * h + x
    eprint('temp1,temp2 ', end=':\n')
    eprint(temp1, temp2)
    print(min(temp1, temp2))
elif a == b:
    print(x)
else:
    temp1 = (h - 1) * y + x
    temp2 = 2 * x * (h - 1) + x
    eprint('temp1,temp2 ', end=':\n')
    eprint(temp1, temp2)
    print(min(temp1, temp2))
