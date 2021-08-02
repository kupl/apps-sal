from functools import lru_cache
from itertools import accumulate
from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush, heappop, heapify
import math
from collections import *
from functools import reduce, cmp_to_key
import sys
input = sys.stdin.readline


M = mod = 10 ** 9 + 7
def factors(n): return sorted(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n): return pow(n, mod - 2, mod)


def li(): return [int(i) for i in input().rstrip('\n').split()]
def st(): return input().rstrip('\n')
def val(): return int(input().rstrip('\n'))
def li2(): return [i for i in input().rstrip('\n')]
def li3(): return [int(i) for i in input().rstrip('\n')]


for _ in range(val()):
    n = val()
    s = st()

    raze = breach = 0

    for ind, i in enumerate(s):

        num = int(i)
        if ind & 1:
            if num & 1 == 0: breach = 1
        else:
            if num & 1: raze = 1

    if n & 1:
        print(1 if raze else 2)
    else:
        print(2 if breach else 1)
