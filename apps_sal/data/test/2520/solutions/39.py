from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(10**6)

N, M, K = map(int, input().split())
F = [list(map(int, input().split())) for _ in range(M)]
B = [list(map(int, input().split())) for _ in range(K)]

class UFTree():
    def __init__(self, n):
        self.length = n+1
        self.roots = list(range(self.length))

    def union(self, a, b):
        r = self.find(a)
        s = self.find(b)
        self.roots[s] = r

    def find(self, a):
        r = self.roots[a]
        if r == a:
            return a
        r = self.find(r)
        self.roots[a] = r
        return r

    def findall(self):
        for i in range(self.length):
            self.find(i)

    def setli(self):
        self.findall()
        d = defaultdict(set)
        for i, r in enumerate(self.roots):
            if i: d[r].add(i)
        return list(d.values())

    def sameroot(self, a, b):
        r = self.find(a)
        s = self.find(b)
        return r == s

t = UFTree(N)
for a, b in F:
    t.union(a, b)

s = [0]*(N+1)
for a, b in F:
    s[a] -= 1
    s[b] -= 1
for c, d in B:
    if t.sameroot(c, d):
        s[c] -= 1
        s[d] -= 1

for u in t.setli():
    l = len(u)
    for i in u: s[i] += l-1

print(*s[1:])
