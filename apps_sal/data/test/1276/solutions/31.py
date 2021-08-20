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
import sys
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


N = ni()
S = ns()
d = {'R': 0, 'G': 0, 'B': 0}
for i in range(N):
    d[S[i]] += 1
ans = 1
for v in d.values():
    ans *= v
for i in range(N):
    for j in range(i + 1, N):
        k = j + (j - i)
        if k >= N:
            break
        if S[i] != S[j] and S[j] != S[k] and (S[i] != S[k]):
            ans -= 1
print(max(ans, 0))
