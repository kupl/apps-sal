import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
from operator import itemgetter

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin


def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))
def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


n = ni()
ab = [na() for _ in range(n)]
ab.sort(key=itemgetter(1, 0))
now = 0
ans = 'Yes'
for i in range(n):
    a, b = ab[i]
    now += a
    if now > b:
        ans = 'No'
        break
print(ans)
