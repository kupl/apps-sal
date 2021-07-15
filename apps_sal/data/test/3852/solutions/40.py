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

from collections import defaultdict, deque, Counter
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

"""
N <= 50
単調増加になるように
いい方法を考える

全てプラス　前から累積
全てマイナス　後ろから累積

プラスとマイナス
全部プラスにするか全部マイナスにするか
プラスのとマイナスのどちらが大きいか

プラスのが大きい
マイナス部分を全てプラスに→前から累積
マイナスのが大きい
プラス部分を全てマイナスに→後ろから累積
det = [-1, 1]
place = [0, 0]
for i in range(N):
    if A[i] > det[0]:
        det[0] = A[i]
        place[0] = i
    elif A[i] < det[1]:
        det[1] = A[i]
        place[1] = i

if abs(det[0]) >= abs(det[1]):
    for i in range(N):
        A[i] += det[0]
    for i in range(1, N):
        A[i] += A[i - 1]
else:
    for i in range(N):
        A[i] += det[1]
    for i in range(N - 2, -1, -1):
        A[i] += A[i + 1]

print(A)
"""

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

# xをyに足す
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
