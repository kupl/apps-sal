from inspect import currentframe
import sys
import os
import time
import re
from pydoc import help
import string
import math
from operator import itemgetter
from collections import Counter
from collections import deque
from collections import defaultdict as dd
import fractions
from heapq import heappop, heappush, heapify
import array
from bisect import bisect_left, bisect_right, insort_left, insort_right
from copy import deepcopy as dcopy
import itertools
sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
GOSA = 1.0 / 10 ** 10
MOD = 10 ** 9 + 7
ALPHABETS = [chr(i) for i in range(ord('a'), ord('z') + 1)]


def LI():
    return [int(x) for x in sys.stdin.readline().split()]


def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]


def LF():
    return [float(x) for x in sys.stdin.readline().split()]


def LS():
    return sys.stdin.readline().split()


def I():
    return int(sys.stdin.readline())


def F():
    return float(sys.stdin.readline())


def DP(N, M, first):
    return [[first] * M for n in range(N)]


def DP3(N, M, L, first):
    return [[[first] * L for n in range(M)] for _ in range(N)]


def solve():
    s = input()
    if s == 'ABC':
        print('ARC')
    else:
        print('ABC')
    return 0


def __starting_point():
    solve()


__starting_point()
