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
sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin


def ni(): return int(ns())
def nf(): return float(ns())
def na(): return list(map(int, stdin.readline().split()))
def nb(): return list(map(float, stdin.readline().split()))
def ns(): return stdin.readline().rstrip()


def judge(S):
    for i in range(len(S) // 2):
        if S[i] != S[-(i + 1)]:
            return False
    return True


S = ns()
N = len(S)
p = S[:(N - 1) // 2]
l = S[(N + 3) // 2 - 1:]
if judge(S) and judge(p) and judge(l):
    print('Yes')
else:
    print('No')
