from scipy.sparse.csgraph import dijkstra
import numpy as np
from itertools import permutations
N, M, R = list(map(int, input().split()))
r = list(map(int, input().split()))

"""
https://juppy.hatenablog.com/entry/2018/11/01/%E8%9F%BB%E6%9C%AC_python_%E5%85%A8%E7%82%B9%E5%AF%BE%E6%9C%80%E7%9F%AD%E7%B5%8C%E8%B7%AF%E6%B3%95%EF%BC%88%E3%83%AF%E3%83%BC%E3%82%B7%E3%83%A3%E3%83%AB%E3%83%95%E3%83%AD%E3%82%A4%E3%83%89%E6%B3%95
"""


def warshall_floyd(d):
    n = len(d)
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


graph = [[float("inf") for i in range(N)] for j in range(N)]
for i in range(M):
    A, B, C = list(map(int, input().split()))
    graph[A - 1][B - 1] = C
    graph[B - 1][A - 1] = C

dist = dijkstra(graph)

ans = 1e10
for i in permutations(r):
    flag = True
    way = list(i)
    tmp = 0
    for i in range(len(way) - 1):
        if dist[way[i] - 1][way[i + 1] - 1] < 0:
            flag = False
            break
        tmp += dist[way[i] - 1][way[i + 1] - 1]
    if flag:
        ans = min(tmp, ans)

print((int(ans)))
