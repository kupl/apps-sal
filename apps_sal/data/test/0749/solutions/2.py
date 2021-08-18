
import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/11/9 23:05

"""

S = input()


def check(s, k):
    for w in set(s):
        c = s[:k].count(w)
        if c == 0:
            continue

        for i in range(k, len(s)):
            if s[i - k] == w:
                c -= 1
            if s[i] == w:
                c += 1
            if c == 0:
                break

        if c > 0:
            return True

    return False


lo = 1
hi = len(S)
while lo < hi:
    m = (lo + hi) // 2
    if check(S, m):
        hi = m
    else:
        lo = m + 1

print(lo)
