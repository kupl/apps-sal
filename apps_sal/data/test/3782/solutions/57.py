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
mod = 10 ** 9 + 7
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

"""
数列A
長さKの連続する部分列を1つ選ぶ　
その中の最小のものを取り除く　infにすれば？
取り除いた要素の最大値 - 最小値をマイナスにしたい　二分探索とかできる?
最終形をイメージする

一番望ましいのは
Q個について最小区間のQ個を取ること
それより小さい要素を取らずに都合のいいとこだけ取りたい
小さい順に仕切りを立てていく
まず小さい順に1 2 3 4...これは必ず取れる　（1 2 3 5...とかは1234より大きくなる）
次に2 3 4 5を取れるか
N個目の数って難しくない？

5 3 2
4 3 1 5 2 の場合
4 3 [1 5 2]
4 [3 5 2]

N <= 2000なので 1, 2, 3, 4で区切っていくのはできそう
Qの中に1を入れる場合、求める値はAq - A1

1 1 3 5 6 7 の場合
1番目の1以降を使うと 1 1 3 5
2番目の1以降を使うと 1 3 5 6
3以降を使うと       3 5 6 7
なので3以降を使う方がいい
Q = 4の時、候補となるのは
[小さい方から1番目、2番目、3番目...] or
[小さい方から2番目、3番目、4番目...] or...

ただし、[小さい方から2番目、3番目、4番目...]を作るには選択範囲に小さい方から1番目を含めないことが必要
4 3 1 5 2 の場合
　　 ×     1は障害物になる
ブロック1:[4, 3]
ブロック2:[5, 2] の中でしかKを回せない
[小さい方から3番目、4番目、5番目...]の場合
ブロック1:[4, 3]
ブロック2:[5]
"""

N, K, Q = getNM()
A = getList()
point = sorted([[A[i], i] for i in range(N)])

flag = [0] * N
ans = float('inf')

for i in range(N):
    s = []
    opt = []
    for j in range(N):
        if flag[j] == 1:  # しきりあれば　
            s = []
        else:  # しきりなければ
            heappush(s, A[j])
            if len(s) >= K:
                opt.append(heappop(s))

    opt.sort()
    if len(opt) >= Q:
        ans = min(ans, opt[Q - 1] - opt[0])
    # 仕切りを立てる
    flag[point[i][1]] = 1

print(ans)
