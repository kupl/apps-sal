from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def root(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            self.parent[x] = y

    def same(self, x, y):
        return self.root(x) == self.root(y)


N, K, L = list(map(int, input().split()))
un1 = UnionFind(N)
for i in range(K):
    p, q = list(map(int, input().split()))
    p -= 1
    q -= 1
    un1.unite(p, q)
un2 = UnionFind(N)
for i in range(L):
    r, s = list(map(int, input().split()))
    r -= 1
    s -= 1
    un2.unite(r, s)
dic = defaultdict(int)
for i in range(N):
    a, b = un1.root(i), un2.root(i)
    k = str(a) + ":" + str(b)
    dic[k] += 1

ans = [0] * N
for i in range(N):
    a, b = un1.root(i), un2.root(i)
    k = str(a) + ":" + str(b)
    ans[i] = dic[k]
print((*ans))
