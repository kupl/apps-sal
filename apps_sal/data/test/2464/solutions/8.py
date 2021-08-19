import sys
input = sys.stdin.readline


class UnionFind:

    def __init__(self, n):
        self.parent = [-1] * n
        self.cnt = n

    def root(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def merge(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.parent[x] > self.parent[y]:
            (x, y) = (y, x)
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        self.cnt -= 1

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def get_size(self, x):
        return -self.parent[self.root(x)]

    def get_cnt(self):
        return self.cnt


n = int(input())
info = [list(map(int, input().split())) for i in range(n - 1)]
uf0 = UnionFind(n)
uf1 = UnionFind(n)
tree0 = [[] for i in range(n)]
tree1 = [[] for i in range(n)]
for i in range(n - 1):
    (a, b, cost) = info[i]
    a -= 1
    b -= 1
    if cost == 0:
        tree0[a].append(b)
        tree0[b].append(a)
        uf0.merge(a, b)
    else:
        tree1[a].append(b)
        tree1[b].append(a)
        uf1.merge(a, b)
ans0 = [0] * n
ans1 = [0] * n
for i in range(n):
    ans0[i] = uf0.get_size(i) - 1
    ans1[i] = uf1.get_size(i) - 1
ans = 0
for i in range(n):
    ans += ans0[i]
    ans += ans1[i]
    ans += ans0[i] * ans1[i]
print(ans)
