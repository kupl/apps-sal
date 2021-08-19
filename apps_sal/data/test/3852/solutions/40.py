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
    return map(int, input().split())


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
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
'\nN <= 50\n単調増加になるように\nいい方法を考える\n\n全てプラス\u3000前から累積\n全てマイナス\u3000後ろから累積\n\nプラスとマイナス\n全部プラスにするか全部マイナスにするか\nプラスのとマイナスのどちらが大きいか\n\nプラスのが大きい\nマイナス部分を全てプラスに→前から累積\nマイナスのが大きい\nプラス部分を全てマイナスに→後ろから累積\ndet = [-1, 1]\nplace = [0, 0]\nfor i in range(N):\n    if A[i] > det[0]:\n        det[0] = A[i]\n        place[0] = i\n    elif A[i] < det[1]:\n        det[1] = A[i]\n        place[1] = i\n\nif abs(det[0]) >= abs(det[1]):\n    for i in range(N):\n        A[i] += det[0]\n    for i in range(1, N):\n        A[i] += A[i - 1]\nelse:\n    for i in range(N):\n        A[i] += det[1]\n    for i in range(N - 2, -1, -1):\n        A[i] += A[i + 1]\n\nprint(A)\n'
N = getN()
A = getList()
det = [-1, 1]
place = [0, 0]
for i in range(N):
    if A[i] > det[0]:
        det[0] = A[i]
        place[0] = i
    elif A[i] < det[1]:
        det[1] = A[i]
        place[1] = i
print(2 * N - 1)
if abs(det[0]) >= abs(det[1]):
    for i in range(N):
        print(place[0] + 1, i + 1)
    for i in range(1, N):
        print(i, i + 1)
else:
    for i in range(N):
        print(place[1] + 1, i + 1)
    for i in range(N - 2, -1, -1):
        print(i + 2, i + 1)
