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
mod = 998244353
'\n数列A\n長さKの連続する部分列を1つ選ぶ\u3000\nその中の最小のものを取り除く\u3000infにすれば？\n取り除いた要素の最大値 - 最小値をマイナスにしたい\u3000二分探索とかできる?\n最終形をイメージする\n\n一番望ましいのは\nQ個について最小区間のQ個を取ること\nそれより小さい要素を取らずに都合のいいとこだけ取りたい\n小さい順に仕切りを立てていく\nまず小さい順に1 2 3 4...これは必ず取れる\u3000（1 2 3 5...とかは1234より大きくなる）\n次に2 3 4 5を取れるか\nN個目の数って難しくない？\n\n5 3 2\n4 3 1 5 2 の場合\n4 3 [1 5 2]\n4 [3 5 2]\n\nN <= 2000なので 1, 2, 3, 4で区切っていくのはできそう\nQの中に1を入れる場合、求める値はAq - A1\n\n1 1 3 5 6 7 の場合\n1番目の1以降を使うと 1 1 3 5\n2番目の1以降を使うと 1 3 5 6\n3以降を使うと       3 5 6 7\nなので3以降を使う方がいい\n'
(N, K, Q) = getNM()
A = getList()
A = [[A[i], i] for i in range(N)]
flag = [0] * N
l = deepcopy(sorted(A))
opt = []
l.sort()
for i in range(Q):
    opt.append(l[i][0])
ans = opt[-1] - opt[0]
for i in range(N):
    flag[l[i][1]] = 1
    parent = []
    child = []
    for j in range(N):
        if flag[j] == 0:
            child.append(A[j][0])
        else:
            child.sort()
            parent.append(child)
            child = []
    if len(child):
        child.sort()
        parent.append(child)
    opt = []
    for array in parent:
        for j in range(len(array) - K + 1):
            opt.append(array[j])
    if len(opt) >= Q:
        opt.sort()
        ans = min(ans, opt[Q - 1] - opt[0])
print(ans)
