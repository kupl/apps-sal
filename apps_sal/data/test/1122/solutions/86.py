from collections import defaultdict, deque, Counter
import sys
from bisect import bisect_left, bisect_right
from functools import reduce
from operator import mul, itemgetter
from itertools import combinations, permutations, product
from copy import deepcopy
import string
import random
import math
from heapq import heapify, heappop, heappush
from decimal import *


def getN():
    return int(input())


def getNM():
    return list(map(int, input().split()))


def getList():
    return list(map(int, input().split()))


def getArray(intn):
    return [int(input()) for i in range(intn)]


def input():
    return sys.stdin.readline().rstrip()


def rand_N(ran1, ran2):
    return random.randint(ran1, ran2)


def rand_List(ran1, ran2, rantime):
    return [random.randint(ran1, ran2) for i in range(rantime)]


def rand_ints_nodup(ran1, ran2, rantime):
    ns = []
    while len(ns) < rantime:
        n = random.randint(ran1, ran2)
        if not n in ns:
            ns.append(n)
    return sorted(ns)


def rand_query(ran1, ran2, rantime):
    r_query = []
    while len(r_query) < rantime:
        n_q = rand_ints_nodup(ran1, ran2, 2)
        if not n_q in r_query:
            r_query.append(n_q)
    return sorted(r_query)


sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
(N, M) = getNM()
A = []
B = []
if N % 2 != 0:
    for i in range(M):
        A.append(i + 1)
        B.append(N - i)
else:
    for i in range(M):
        A.append(i + 1)
        if i <= N // 4 - 1:
            B.append(N - i)
        else:
            B.append(N - i - 1)
for i in range(M):
    print((A[i], B[i]))
