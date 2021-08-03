import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
import functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]


def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    N, M, S = LI()
    G = [[[] for _ in range(2501)] for _ in range(N)]

    for i in range(M):
        u, v, a, b = LI()
        u -= 1
        v -= 1
        for money in range(2501):
            if money - a < 0:
                continue
            G[u][money].append((b, v, money - a))
            G[v][money].append((b, u, money - a))

    for i in range(N):
        c, d = LI()
        for money in range(2501):
            new_money = min(2500, money + c)
            G[i][money].append((d, i, new_money))

    def dijkstra(u, s):
        q = []
        d = [[inf for __ in range(2501)] for _ in range(N)]
        visited = set()
        dist = 0
        money = min(2500, s)
        d[u][money] = dist
        heapq.heappush(q, (dist, u, money))
        while len(q) > 0:
            dist, u, u_money = heapq.heappop(q)

            if (u, u_money) in visited:
                continue
            visited.add((u, u_money))
            for next_node_tuple in G[u][u_money]:
                cost, v, v_money = next_node_tuple
                if dist + cost < d[v][v_money]:
                    d[v][v_money] = dist + cost
                    heapq.heappush(q, (d[v][v_money], v, v_money))
        return d
    d = dijkstra(0, S)
    for i in range(1, N):
        print((min(d[i])))


main()
