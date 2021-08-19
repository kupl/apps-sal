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


H, W = zz()
board = []
for h in range(H):
    board.append(list(input()))
board = np.array(board)
ans1 = []
for h in range(H):
    if ('#' in board[h]):
        ans1.append(board[h])
ans2 = []
board = np.array(ans1)
for w in range(W):
    if ('#' in board[:, w]):
        ans2.append(board[:, w])
ans2 = np.array(ans2).T

for line in ans2:
    print(*line, sep='')
