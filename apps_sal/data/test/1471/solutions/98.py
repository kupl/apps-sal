#import math
#import itertools
from collections import deque


def INT(): return int(input())


def INTM(): return map(int, input().split())
def STRM(): return map(str, input().split())
def STR(): return str(input())


def LIST(): return list(map(int, input().split()))
def LISTS(): return list(map(str, input().split()))


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = [[] for _ in range(v)]
        self.INF = 10 ** 9

    def addEdge(self, start, end, dist):
        self.graph[start].append((end, dist))
        self.graph[end].append((start, dist))


def do():
    n = INT()
    g = Graph(n)
    for i in range(n - 1):
        u, v, d = INTM()
        u -= 1
        v -= 1
        g.addEdge(u, v, d)

    que = deque()
    check = [True] * n
    dists = [-1] * n
    check[0] = False
    dists[0] = 0
    que.append([0, 0])
    while que:
        now, dist_f = que.popleft()
        for next, dist in g.graph[now]:
            if check[next]:
                check[next] = False
                temp = dist_f + dist
                dists[next] = temp
                que.append([next, temp])

    for i in dists:
        if i % 2 == 0:
            print(0)
        else:
            print(1)


def __starting_point():
    do()


__starting_point()
