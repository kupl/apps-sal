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


def check(s):
    if (s[len(s) // 2:] == s[:len(s) // 2]):
        print((len(s)))
        return


S = S()
n = len(S)
if (n % 2 == 0):
    while S:
        S = S[:-2]
        check(S)
else:
    S = S[:-1]
    check(S)
    while S:
        S = S[:-2]
        check(S)

