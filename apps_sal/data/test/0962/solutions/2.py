# find a cycle
import sys


def find_cycle(g):
    n = len(g)
    used = [0] * n  # 0:not yet 1: visiting 2: visited
    for v in range(n):  # 各点でDFS
        if used[v] == 2:
            continue
        # 初期化
        stack = [v]
        hist = []  # 履歴
        while stack:
            v = stack[-1]
            if used[v] == 1:
                used[v] = 2  # 帰りがけの状態に
                stack.pop()
                hist.pop()
                continue
            hist.append(v)
            used[v] = 1  # 行きがけの状態に
            for c in g[v]:
                if used[c] == 2:
                    continue
                elif used[c] == 1:  # cを始点とするサイクル発見！
                    return hist[hist.index(c):]
                else:
                    stack.append(c)
    return None


def find_minimal_cycle(g, cycle):
    n = len(g)
    is_in_cycle = [0] * n  # サイクルに使われているか
    nxt = [-1] * n  # 次の頂点

    l = len(cycle)
    for i, c in enumerate(cycle):
        is_in_cycle[c] = 1
        nxt[c] = cycle[i + 1 - l]

    # 極小サイクルを求める
    for v in cycle:
        if is_in_cycle[v]:
            for c in g[v]:
                if is_in_cycle[c] == 1:  # もしショートカット v -> c があれば
                    v0 = nxt[v]  # 以下サイクルのうち v から c までを削除
                    while v0 != c:
                        is_in_cycle[v0] = 0
                        v0 = nxt[v0]
                    nxt[v] = c  # nxt を繋ぎ直す

    # 極小サイクルの出力
    i = is_in_cycle.index(1)
    v = nxt[i]
    hist = [i]  # 履歴
    while v != i:
        hist.append(v)
        v = nxt[v]
    return hist


#########################################################

##########################################################
# coding: utf-8
# Your code here!
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline

n, m = [int(i) for i in readline().split()]
g = [[] for _ in range(n)]

for _ in range(m):
    a, b = [int(i) - 1 for i in readline().split()]
    g[a].append(b)

cycle = find_cycle(g)

if cycle == None:
    print((-1))
else:
    res = find_minimal_cycle(g, cycle)
    print((len(res)))
    for i in res:
        print((i + 1))
