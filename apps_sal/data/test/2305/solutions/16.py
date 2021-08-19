#!/usr/bin/env python3
from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")
MOD = 10**9 + 7


class Graph(object):
    def __init__(self, N):
        self.N = N
        self.E = defaultdict(list)

    def add_edge(self, f, t, w=1):
        self.E[f].append((t, w))
        self.E[t].append((f, w))


N = int(input())
c = [x - 1 for x in map(int, input().split())]
A = [None] * (N - 1)
B = [None] * (N - 1)
for i in range(N - 1):
    A[i], B[i] = list(map(int, input().split()))

g = Graph(N)
for a, b in zip(A, B):
    g.add_edge(a - 1, b - 1)

# k=1, 2, ..., Nに対して
# 色kが塗られている頂点を一度以上通るような単純パスの数を求める
# 全パスの個数 - 色kが塗られている頂点を一度も通らない単純パスの数
# 全パスの個数はN*(N+1)/2

# グラフを色kのノードで分割して、部分グラフ内での単純パスの総数を求めれば良い
# 各ノードに状態として辞書をもたせる。
# x辞書は色iを通らずに到達可能な頂点の数を持つ。
# o辞書は色iを通らずに到達不可能な頂点の数を持つ。

# 回答用
ans = [0] * N


def f(curr, par=-1):
    # 再帰関数
    # curr: 現在の節点
    # par : 親節点の番号
    ret = defaultdict(int)
    size = 1
    for dest, w in g.E[curr]:
        if dest == par:
            continue
        sz, child = f(dest, curr)
        size += sz

        # 自身の色と同じ場合、子の頂点の数から加算
        n = sz - child[c[curr]]
        ans[c[curr]] += n * (n + 1) // 2

        # マージ
        if len(ret) < len(child):
            child, ret = ret, child
        for key in child:
            ret[key] += child[key]

    ret[c[curr]] = size
    return size, ret


sz, ret = f(0)
for color in range(N):
    if color != c[0]:
        n = sz - ret[color]
        ans[color] += n * (n + 1) // 2

tot = N * (N + 1) // 2
for a in ans:
    print((tot - a))
