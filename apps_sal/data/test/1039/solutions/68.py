import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys
input = lambda: sys.stdin.readline().rstrip()
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
        a, b, c = LI()
        G[a - 1].append((b - 1, c))
        G[b - 1].append((a - 1, c))
    Q, K = LI()
    K -= 1

    dist = [-1] * N
    dist[K] = 0
    que = collections.deque()
    que.append(K)
    while que:
        c = que.popleft()
        for n, l in G[c]:
            if dist[n] == -1:
                dist[n] = dist[c] + l
                que.append(n)

    for _ in range(Q):
        x, y = LI_()
        ans = dist[x] + dist[y]
        print(ans)


def __starting_point():
    resolve()


__starting_point()
