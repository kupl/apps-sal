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


N = ni()
a = [2, 4, 5, 7, 9]
b = [0, 1, 6, 8]
c = [3]
r = N % 10
if r in a:
    print('hon')
elif r in b:
    print('pon')
else:
    print('bon')
