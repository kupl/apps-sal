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
    return sorted(range(len(ls)), key=ls.__getitem__)


def f(p=0):
    if p == 1:
        return map(int, input().split())
    elif p == 2:
        return list(map(int, input().split()))
    elif p == 3:
        return list(input())
    else:
        return int(input())


class DisjointSet:
    _disjoint_set = list()

    def __init__(self, init_arr):
        self._disjoint_set = []
        if init_arr:
            for item in list(set(init_arr)):
                self._disjoint_set.append([item])

    def _find_index(self, elem):
        for item in self._disjoint_set:
            if elem in item:
                return self._disjoint_set.index(item)
        return None

    def find(self, elem):
        for item in self._disjoint_set:
            if elem in item:
                return self._disjoint_set[self._disjoint_set.index(item)]
        return None

    def union(self, elem1, elem2):
        index_elem1 = self._find_index(elem1)
        index_elem2 = self._find_index(elem2)
        if index_elem1 != index_elem2 and index_elem1 is not None and index_elem2 is not None:
            self._disjoint_set[index_elem2] = self._disjoint_set[index_elem2] + self._disjoint_set[index_elem1]
            del self._disjoint_set[index_elem1]
        return self._disjoint_set

    def get(self):
        return self._disjoint_set


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
    print(u)
    visited[u] = 1
    for v in g[u]:
        if visited[v] == 0:
            dfs(v, g, visited)


t = f()
for i in range(t):
    n = f()
    cl = f(2)
    count = 0
    a = 0
    b = 0
    for i in range(n):
        if cl[i]%3==0:
            count+=1
        elif cl[i]%3==1:
            a+=1
        else:
            b+=1

    print(count+min(a, b)+(max(a, b) - min(a, b))//3)
