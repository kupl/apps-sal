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

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin


def ni(): return int(ns())
def nf(): return float(ns())
def na(): return list(map(int, stdin.readline().split()))
def nb(): return list(map(float, stdin.readline().split()))
def ns(): return stdin.readline().rstrip()


A, B, N = na()
if N >= B - 1:
    print(math.floor(A * (B - 1) / B) - A * math.floor((B - 1) / B))
else:
    print(math.floor(A * (N) / B) - A * math.floor((N) / B))
