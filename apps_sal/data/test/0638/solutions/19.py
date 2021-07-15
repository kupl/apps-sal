import math
import bisect
import heapq
from collections import defaultdict


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)


def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n


def isprime(n):
    for d in range(2, int(math.sqrt(n))+1):
        if n % d == 0:
            return False
    return True


def argsort(ls):
    return sorted(list(range(len(ls))), key=ls.__getitem__)


def f(p=0):
    if p == 1:
        return list(map(int, input().split()))
    elif p == 2:
        return list(map(int, input().split()))
    elif p == 3:
        return list(input())
    else:
        return int(input())


class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(1, n+1)]
        self.rank = [0]*(n+1)

    def find_set(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find_set(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        set_x = self.find_set(x)
        set_y = self.find_set(y)
        if set_x!=set_y:
            if self.rank[x]:
                pass


def graph(n, m, edg=False):
    edges = []
    visited = [0]*n
    g = [list() for _ in range(n+1)]
    for i in range(m):
        u, v = f(1)
        g[u].append(v)
        g[v].append(u)
        if edg:
            edges.append((u, v))

    if edg:
        return g, visited, edg
    else:
        return g, visited


def bfs(g, visited):
    queue = [1]
    visited[1] = 1
    for u in queue:
        for v in g[u]:
            if visited[v] == 0:
                queue.append(v)
            visited[v] = 1


def dfs(u, g, visited):
    visited[u] = 1
    for v in g[u]:
        if visited[v] == 0:
            dfs(v, g, visited)


n, t = f(1)

cl = f(2)
pl = []
count = 0
sm = 0

res= []

for i in range(n):
    sm += cl[i]
    k = t-sm
    j = count-1
    while(j>-1 and k<0):
        k+=pl[j]
        j-=1

    if k<0:
        res.append(count)
    else:
        res.append(count-j-1)

    bisect.insort(pl, cl[i])
    count+=1

print(*res)

