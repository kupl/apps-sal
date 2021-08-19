import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x) - 1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()


def resolve():
    N = I()
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = LI()
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))

    # print(G)

    ans = [-1] * N
    ans[0] = 0
    visited = [False] * N

    def dfs(c):
        visited[c] = True
        for n, w in G[c]:
            if not visited[n]:
                if w % 2 == 0:
                    ans[n] = ans[c]
                else:
                    ans[n] = 1 - ans[c]
                dfs(n)

    dfs(0)

    for i in ans:
        print(i)


def __starting_point():
    resolve()


__starting_point()
