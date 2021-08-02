from heapq import heapify, heappop, heappush
from functools import lru_cache  # pypyでもうごく
from itertools import accumulate  # 累積和
from collections import Counter  # 文字列を個数カウント辞書に、
from bisect import bisect_left, bisect, bisect_right  # 2分探索
from collections import deque
from operator import itemgetter
from copy import deepcopy as dcp
from copy import copy, deepcopy
import math
import sys
sys.setrecursionlimit(10**7)  # 再帰関数の上限,10**5以上の場合python
# bisect_left(l,x), bisect(l,x)#aはソート済みである必要あり。aの中からx未満の要素数を返す。rightだと以下
#deque(l), pop(), append(x), popleft(), appendleft(x)
# listでqueの代用をするとO(N)の計算量がかかってしまうので注意
# S=Counter(l),S.most_common(x),S.keys(),S.values(),S.items()
# list(accumulate(l))
# heapify(q),heappush(q,a),heappop(q) #q=heapify(q)としないこと、返り値はNone
# import fractions#古いatcoderコンテストの場合GCDなどはここからimportする
# @lru_cache(maxsize = None)#maxsizeは保存するデータ数の最大値、2**nが最も高効率


def input(): return sys.stdin.readline()[:-1]
def printl(li): _ = print(*li, sep="\n") if li else None


def argsort(s, return_sorted=False):
    inds = sorted(range(len(s)), key=lambda k: s[k])
    if return_sorted: return inds, [s[i] for i in inds]
    return inds


def alp2num(c, cap=False): return ord(c) - 97 if not cap else ord(c) - 65
def num2alp(i, cap=False): return chr(i + 97) if not cap else chr(i + 65)


def matmat(A, B):
    K, N, M = len(B), len(A), len(B[0])
    return [[sum([(A[i][k] * B[k][j]) for k in range(K)]) for j in range(M)] for i in range(N)]


def matvec(M, v):
    N, size = len(v), len(M)
    return [sum([M[i][j] * v[j] for j in range(N)]) for i in range(size)]


def T(M):
    n, m = len(M), len(M[0])
    return [[M[j][i] for j in range(n)] for i in range(m)]


def main():
    mod = 1000000007
    # w.sort(key=itemgetter(1),reversed=True)  #二個目の要素で降順並び替え

    #N = int(input())
    N, Q = map(int, input().split())
    # A = tuple(map(int, input().split())) #1行ベクトル
    # L = tuple(int(input()) for i in range(N)) #改行ベクトル
    # S = tuple(tuple(map(int, input().split())) for i in range(N)) #改行行列

    l = [Counter() for _ in range(2 * 10**5)]
    rates = [[] for _ in range(2 * 10**5)]
    dic = dict()
    for i in range(N):
        a, b = map(int, input().split())
        b -= 1
        l[b][a] += 1
        dic[i] = (a, b)
        heappush(rates[b], -a)
    tot = []
    for b, r in enumerate(rates):
        if r:
            a = -r[0]
            heappush(tot, (a, b))

    qs = tuple(tuple(map(int, input().split())) for i in range(Q))
    for c, d in qs:
        c -= 1
        d -= 1
        a, b = dic[c]
        l[b][a] -= 1
        l[d][a] += 1
        dic[c] = (a, d)
        heappush(rates[d], -a)
        heappush(tot, (a, d))
        rm = -rates[b][0]
        while rates[b] and l[b][-rates[b][0]] == 0:
            heappop(rates[b])

        if rates[b]:
            heappush(tot, (-rates[b][0], b))

        m, mb = tot[0]
        # print(l[0],l[1],l[2])
        while l[mb][m] < 1 or m != -rates[mb][0]:
            heappop(tot)

            m, mb = tot[0]

        print(m)


def __starting_point():
    main()


__starting_point()
