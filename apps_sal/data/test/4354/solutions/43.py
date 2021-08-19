# -*- coding: utf-8 -*-
import numpy as np
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect
from scipy.special import comb
import copy
sys.setrecursionlimit(10**6)


def zz():
    return list(map(int, sys.stdin.readline().split()))


def z():
    return int(sys.stdin.readline())


def S():
    return sys.stdin.readline()[:-1]


def C(line):
    return [sys.stdin.readline() for _ in range(line)]


n, m = zz()
A, B = [], []
for i in range(n):
    a, b = zz()
    A.append(a)
    B.append(b)
C, D = [], []
for i in range(m):
    c, d = zz()
    C.append(c)
    D.append(d)

dist = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        dist[i][j] = abs(A[i] - C[j]) + abs(B[i] - D[j])


for i in range(n):
    print((np.argmin(dist[i]) + 1))
