import sys


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


def input():
    return sys.stdin.readline().strip()


(n, k, l) = map(int, input().split())
road = UnionFind(n)
rail = UnionFind(n)
for _ in range(k):
    (p, q) = map(int, input().split())
    road.union(p - 1, q - 1)
for _ in range(l):
    (r, s) = map(int, input().split())
    rail.union(r - 1, s - 1)
dic = {}
l = []
for i in range(n):
    tup = (road.find(i), rail.find(i))
    l.append(tup)
    if tup in dic:
        dic[tup] += 1
    else:
        dic[tup] = 1
ans = []
for i in l:
    ans.append(dic[i])
print(' '.join(map(str, ans)))
