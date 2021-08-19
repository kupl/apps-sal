"""
Created on Sat Apr 20 20:47:47 2019

@author: Owner
"""
import numpy as np
import sys
import collections
import scipy.misc
import math
from operator import itemgetter
import itertools
import copy
import bisect
import heapq


def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n /= i
            table.append(int(i))
        i += 1
    if n > 1:
        table.append(int(n))
    return table


def digit(i):
    if i > 0:
        return digit(i // 10) + [i % 10]
    else:
        return []


def getNearestValueIndex(list, num):
    """
    概要: リストからある値に最も近い値のインデックスを取得する関数
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    """
    idx = np.abs(np.asarray(list) - num).argmin()
    return idx


def find_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default


class UnionFind(object):

    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        """
        x が属するグループを探索
        """
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        """
        x と y のグループを結合
        """
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                (x, y) = (y, x)
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y]

    def is_same(self, x, y):
        """
        x と y が同じグループか否か
        """
        return self.find(x) == self.find(y)

    def get_size(self, x):
        """
        x が属するグループの要素数
        """
        x = self.find(x)
        return self.size[x]


"\nN, X = map(int, input().split())\n\nx = list(map(int, input().split()))\n\nP = [0]*N\nY = [0]*N\nfor n in range(N):\n    P[n], Y[n] = map(int, input().split())\n\n# 多次元配列の宣言（あとでintにすること。）（タプルにすること。）\ndp = np.zeros((N+1, 4,4,4))\n    \nall(nstr.count(c) for c in '753')\n\n# 複数配列を並び替え\nABT = zip(A, B, totAB)\nresult = 0\n# itemgetterには何番目の配列をキーにしたいか渡します\nsorted(ABT,key=itemgetter(2))\nA, B, totAB = zip(*ABT)\nA.sort(reverse=True)\n\n# 2進数のbit判定\n(x >> i) & 1\n\n# dp最小化問題\ndp = [np.inf]*N\nfor n in range(N):\n    if n == 0:\n        dp[n] = 0\n    else:\n        for k in range(1,K+1):\n            if n-k >= 0:\n                dp[n] = min(dp[n], dp[n-k] + abs(h[n]-h[n-k]))\n            else:\n                break\n# 累積和\nadd = 1 # 問題によって決まる\nres = 0\nsums = [0]*(len(nums)+1)\nfor i in range(len(nums)):\n    sums[i+1] = sums[i] + nums[i]\nfor i in range(0, len(nums), 2):\n    left = i\n    right = min(i+add, len(nums))\n    tmp = sums[right] - sums[left]\n    res = max(tmp, res)\n\n#２分探索\nli, ri = bisect.bisect_left(p_ac, l[i]-1), bisect.bisect_right(p_ac, r[i]-1)    \n\n#ソート関数\norg_list = [3, 1, 4, 5, 2]\nnew_list = sorted(org_list)\nprint(org_list)\nprint(new_list)\n# [3, 1, 4, 5, 2]\n# [1, 2, 3, 4, 5]\n\n#Distance Transformation\n    for h in range(0,H):\n        for w in range(0,W):\n            if h == 0 and w == 0:\n                pass\n            elif h == 0:\n                D[H-h-1][W-w-1]= min(D[H-h-1][W-w-1], D[H-h-1][W-w]+1)\n            elif w == 0:   \n                D[H-h-1][W-w-1]= min(D[H-h-1][W-w-1], D[H-h][W-w-1]+1)\n            else:\n                D[H-h-1][W-w-1]= min(D[H-h-1][W-w-1], D[H-h][W-w-1]+1, D[H-h-1][W-w]+1, D[H-h][W-w]+2)\n            d_max = max(D[H-h-1][W-w-1], d_max)\n\n"


def bfs(n):
    clsd = set()
    opnd = collections.deque()
    root = [None] * N
    d_list = [0] * N
    opnd.append(n)
    while len(opnd) != 0:
        now = opnd.popleft()
        clsd.add(now)
        for e in E[now]:
            if e in clsd:
                if e == n:
                    res = [now]
                    dist = d_list[now] + 1
                    while len(res) != dist:
                        res.append(root[res[-1]])
                    return [list(reversed(res)), dist]
            else:
                opnd.append(e)
                root[e] = now
                d_list[e] = d_list[root[e]] + 1
    return [[], inf]


(N, M) = list(map(int, input().split()))
E = [[] for n in range(N)]
for m in range(M):
    e = list(map(int, input().split()))
    E[e[0] - 1].append(e[1] - 1)
inf = 10 ** 9


def main():
    res = []
    d_min = inf
    for n in range(N):
        (graph, dist) = bfs(n)
        if dist < d_min:
            d_min = dist
            res = graph
    if d_min != inf:
        print(d_min)
        for n in range(d_min):
            print(res[n] + 1)
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()
