# Union Find 木
from sys import setrecursionlimit

# 要素xが属するグループの根を返す


def find(parent, i):
    t = parent[i]
    if t < 0:
        return i
    t = find(parent, t)
    parent[i] = t
    return t

# xとyの木を併合


def unite(parent, i, j):
    i = find(parent, i)
    j = find(parent, j)
    if i == j:
        return
    parent[j] += parent[i]
    parent[i] = j


setrecursionlimit(10 ** 6)

N, M = list(map(int, input().split()))
AB = [[int(c) - 1 for c in input().split()] for _ in range(M)]
# print(AB[::-1])

parent = [-1] * N
inconvenience = N * (N - 1) // 2
result = []
for a, b in AB[::-1]:
    # print(inconvenience)
    # print(parent)
    result.append(inconvenience)

    #a, bが属するグループの根をparentに記録する
    pa, pb = find(parent, a), find(parent, b)
    # print(pa, pb)
    # print(parent[pa], parent[pb], parent[pa] * parent[pb])

    #
    if pa != pb:
        inconvenience -= parent[pa] * parent[pb]

    # 取り出した辺を併合
    unite(parent, a, b)

print((*result[::-1]))
