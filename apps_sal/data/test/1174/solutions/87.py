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
sys.setrecursionlimit(10 ** 6)


def zz():
    return list(map(int, sys.stdin.readline().split()))


def z():
    return int(sys.stdin.readline())


def S():
    return sys.stdin.readline()[:-1]


def C(line):
    return [sys.stdin.readline() for _ in range(line)]


(N, M) = zz()
A = zz()
A = [-a for a in A]
heapq.heapify(A)
for i in range(M):
    money = heapq.heappop(A)
    money *= -1
    money //= 2
    money *= -1
    heapq.heappush(A, money)
print(sum(A) * -1)
