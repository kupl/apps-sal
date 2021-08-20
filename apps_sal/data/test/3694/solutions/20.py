import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List
'\ncreated by shhuan at 2020/1/8 22:06\n\n'


def solve(N, A):
    wc = collections.Counter(A)
    if wc[0] > 1:
        return False
    if any([v > 2 for v in wc.values()]):
        return False
    if len([v for v in wc.values() if v > 1]) > 1:
        return False
    if any([c > 1 and w - 1 in wc for (w, c) in wc.items()]):
        return False
    taken = sum(A) - N * (N - 1) // 2
    return taken % 2 != 0


N = int(input())
A = [int(x) for x in input().split()]
s = solve(N, A)
print('sjfnb' if s else 'cslnb')
