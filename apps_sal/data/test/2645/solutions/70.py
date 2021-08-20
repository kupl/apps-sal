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
import bisect
from operator import itemgetter
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
mod = 10 ** 9 + 7
stdin = sys.stdin


def ni():
    return int(ns())


def nf():
    return float(ns())


def na():
    return list(map(int, stdin.readline().split()))


def nb():
    return list(map(float, stdin.readline().split()))


def ns():
    return stdin.readline().rstrip()


s = ns()
ans = 0
ct = 0
for i in range(len(s)):
    if ct == 0:
        ct += 1
        if s[i] == 'p':
            ans -= 1
    else:
        ct -= 1
        if s[i] == 'g':
            ans += 1
print(ans)
