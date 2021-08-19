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


(H, W) = na()
N = ni()
a = na()
ans = []
for i in range(N):
    for _ in range(a[i]):
        ans.append(i + 1)
for i in range(H):
    if i % 2 == 0:
        print(*ans[i * W:(i + 1) * W])
    else:
        print(*ans[i * W:(i + 1) * W][::-1])
