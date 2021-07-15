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

#############
# Main Code #
#############

"""
最長増加部分列の長さはA　
最長減少部分列の長さはB
使える数字は1 ~ N
一番都合のいいものを探す
A + B > N + 1ならダメっぽい
A + B = Nの場合
2 3 5 + 5 4
2 3 1 5 4
1を適当な所に置けば良い
A + B = N + 1の場合は簡単
N = 5
A, B = 3, 3
3 4 5 + 5 2 1
3 4 5 2 1

A + B < N の場合
いらないものを適当に置けば
いいのでは？
N = 5
A, B = 2, 2 は無理 A + B <= 4は無理
2 3 + 3 1 (4, 5はいらない)
2 3 1 + 4 5

(5, 6, 3, 1, 4, 2)
4 5 6 1 2 3

def lis(A):
    L = [A[0]]
    for a in A[1:]:
        if a > L[-1]:
            L.append(a)
        # このelseに引っかかった時にトランプのソートが必要
        else:
            L[bisect_left(L, a)] = a
    return len(L)

for i in permutations([1, 2, 3, 4, 5, 6, 7]):
    if lis(i) + lis(list(reversed(i))) <= 5:
        print(lis(i), lis(list(reversed(i))), i)

相方を2にした場合の下限は(N + 1) // 2 ?
5なら3 2
6なら3 2
7なら4 2
8なら4 2
3 4 5 + 5 2
3 4 5 1 2
4 5 6 + 6 3
4 5 6 1 2 3
4 5 6 7 + 6 3
4 5 6 7 1 2 3
細かく区切ればもっといける
N = 16なら
[13 14 15 16] [9 10 11 12] [5 6 7 8] [1 2 3 4]
A = 4, B = 4
A * B >= Nであれば作れる
"""

N, A, B = getNM()

# mainの長さが半分より下ならout
if A * B < N or N + 1 < A + B:
    print(-1)
    return

if A == 1:
    if B == N:
        print(*[i for i in range(N, 0, -1)])
    else:
        print(-1)
    return

if B == 1:
    if A == N:
        print(*[i for i in range(1, N + 1)])
    else:
        print(-1)
    return

# グループ内の要素の数がA,グループの数がB
res1 = [i + 1 for i in range(N - A, N)]
res2 = []
L = [i + 1 for i in range(N - A - 1, -1, -1)] # 残りN - A個

# 残りN - A個をB - 1個で分割する
ind = (N - A) // (B - 1)
for i in range(B - 1):
    opt = []
    for j in range(ind + (i < (N - A) % (B - 1))):
        u = L.pop()
        opt.append(u)
    res2.append(opt)

res2 = list(reversed(res2))

ans = res1
for i in range(B - 1):
    ans += res2[i]

def lis(A):
    L = [A[0]]
    for a in A[1:]:
        if a > L[-1]:
            L.append(a)
        # このelseに引っかかった時にトランプのソートが必要
        else:
            L[bisect_left(L, a)] = a
    return len(L)

# print(lis(ans), lis(list(reversed(ans))))
print(*ans)
