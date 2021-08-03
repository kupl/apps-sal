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


N = z()
T, X, Y = [], [], []
pos_x, pos_y, now_t = 0, 0, 0
for i in range(N):
    t, x, y = zz()
    T.append(t)
    X.append(x)
    Y.append(y)
ok = 1
for t, x, y in zip(T, X, Y):
    if (abs(x - pos_x) + abs(y - pos_y) > (t - now_t)):
        ok = 0
        break
    if (((abs(x - pos_x) + abs(y - pos_y)) % 2) != ((t - now_t) % 2)):
        ok = 0
        break
    pos_x, pos_y, now_t = x, y, t
if(ok == 1):
    print('Yes')
else:
    print('No')
