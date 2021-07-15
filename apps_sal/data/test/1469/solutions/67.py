#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 終了後に解説を見て解けた
# パス数が２のべき乗であれば簡単にグラフを構築できることに気付きたかった。
#
# 本番中は、10進法で考えて 頂点1と頂点2の間を辺{0, 100, 200, ..., 900}で繋ぎ、頂点2と頂点3の間を辺{0, 10, ..., 90}で繋ぎ、
# などという事を考えていたが、それ以上進展させることが難しかった。


import array
from bisect import *
from collections import *
import fractions
import heapq 
from itertools import *
import math
import random
import re
import string
import sys

L = int(input())

v = 1
edges = []  # (from, to, cost)

# L = 37の場合を例にとりコメントを付与
# まず長さ0 ~ 31までのパスを作成する。
#   頂点1 -> 頂点2を0の辺と1の辺で結ぶ
#   頂点2 -> 頂点3を0の辺と2の辺で結ぶ
#   頂点3 -> 頂点4を0の辺と4の辺で結ぶ
#   頂点4 -> 頂点5を0の辺と8の辺で結ぶ
#   頂点5 -> 頂点6を0の辺と16の辺で結ぶ
n = 2
cost = 1
while n <= L:
    edges.append((v, v+1, 0))
    edges.append((v, v+1, cost))
    cost *= 2
    v += 1
    n *= 2

# 頂点6をv_sink(最終到達点)とする
v_sink = v

# ここから先、長さ32, 33, 34, 35, 36のパスを生成することになる。
# 頂点3と頂点6を、32の辺で直でつなぐと、長さ32, 33, 34, 35のパスが作れる。
# 頂点1と頂点6を、36の辺で直でつなぐと、長さ36のパスが作れる。
n //= 2
N = n
L -= N

while L > 0:
    if L >= n:
        edges.append((v, v_sink, N))
        L -= n
        N += n
    n //= 2
    v -= 1

print(v_sink, len(edges))
for e in edges:
    print(*e)
