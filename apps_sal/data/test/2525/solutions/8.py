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

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin


def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))
def ns(): return stdin.readline().rstrip()


ans = collections.deque(ns())
q = ni()
now = 0
for i in range(q):
    query = ns().split(' ')
    if query[0] == '1':
        now = 1 - now
    else:
        f, c = query[1], query[2]
        if f == '1':
            if now == 1:
                ans.append(c)
            else:
                ans.appendleft(c)
        else:
            if now != 1:
                ans.append(c)
            else:
                ans.appendleft(c)

if now == 1:
    for i in range(len(ans)):
        print(ans[-(i + 1)], end="")
else:
    for i in range(len(ans)):
        print(ans[i], end="")
print()
