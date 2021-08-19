import sys
import heapq
import re
from itertools import permutations
from bisect import bisect_left, bisect_right
from collections import Counter, deque
from fractions import gcd
from math import factorial, sqrt, ceil
from functools import lru_cache, reduce
INF = 1 << 60
MOD = 1000000007
sys.setrecursionlimit(10 ** 7)


class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            (x, y) = (y, x)
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for (i, x) in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join(('{}: {}'.format(r, self.members(r)) for r in self.roots()))


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def warshall_floyd(d, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


def dijkstra_heap(s, edge, n):
    d = [10 ** 20] * n
    used = [True] * n
    d[s] = 0
    used[s] = False
    edgelist = []
    for (a, b) in edge[s]:
        heapq.heappush(edgelist, a * 10 ** 6 + b)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        if not used[minedge % 10 ** 6]:
            continue
        v = minedge % 10 ** 6
        d[v] = minedge // 10 ** 6
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist, (e[0] + d[v]) * 10 ** 6 + e[1])
    return d


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


def lcm(x, y):
    return x * y // gcd(x, y)


def lcm_list(numbers):
    return reduce(lcm, numbers, 1)


def gcd_list(numbers):
    return reduce(gcd, numbers)


def eratosthenes(limit):
    A = [i for i in range(2, limit + 1)]
    P = []
    while True:
        prime = min(A)
        if prime > sqrt(limit):
            break
        P.append(prime)
        i = 0
        while i < len(A):
            if A[i] % prime == 0:
                A.pop(i)
                continue
            i += 1
    for a in A:
        P.append(a)
    return P


def permutation_with_duplicates(L):
    if L == []:
        return [[]]
    else:
        ret = []
        S = sorted(set(L))
        for i in S:
            data = L[:]
            data.remove(i)
            for j in permutation_with_duplicates(data):
                ret.append([i] + j)
        return ret


(n, m) = list(map(int, input().split()))
d = [[INF for j in range(n)] for i in range(n)]
x = []
for i in range(m):
    (a, b, c) = list(map(int, input().split()))
    x.append([a - 1, b - 1, c])
    d[a - 1][b - 1] = c
    d[b - 1][a - 1] = c
d2 = warshall_floyd(d, n)
ans = 0
for i in x:
    if d2[i[0]][i[1]] != i[2]:
        ans += 1
print(ans)
