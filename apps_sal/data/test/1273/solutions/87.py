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
    for i in range(N - 1):
        a, b = LI_()
        G[a].append((b, i))
        G[b].append((a, i))

    ans = [0] * (N - 1)
    visited = [False] * N

    def dfs(c, color_p):
        visited[c] = True
        color = 0
        for n, i in G[c]:
            if not visited[n]:
                if color == color_p:
                    color += 1
                ans[i] = color
                dfs(n, color)
                color += 1

    dfs(0, -1)

    print((max(ans) + 1))
    for i in ans:
        print((i + 1))


def __starting_point():
    resolve()


__starting_point()
