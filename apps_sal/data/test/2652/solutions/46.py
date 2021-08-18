import sys
sys.setrecursionlimit(10**9)


class UnionFind:
    def __init__(self, n):
        self.n = [-1] * n
        self.r = [0] * n
        self.siz = n

    def find_root(self, x):
        if self.n[x] < 0:
            return x
        else:
            self.n[x] = self.find_root(self.n[x])
            return self.n[x]

    def unite(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return
        elif self.r[x] > self.r[y]:
            self.n[x] += self.n[y]
            self.n[y] = x
        else:
            self.n[y] += self.n[x]
            self.n[x] = y
            if self.r[x] == self.r[y]:
                self.r[y] += 1
        self.siz -= 1

    def root_same(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def count(self, x):
        return -self.n[self.find_root(x)]

    def size(self):
        return self.siz


n = int(input())
xy = [list(map(int, input().split())) + [i] for i in range(n)]
G = []

xy.sort()
for j in range(1, n):
    sx, sy, si = xy[j - 1]
    tx, ty, ti = xy[j]
    G.append((min(abs(sx - tx), abs(sy - ty)), si, ti))

xy.sort(key=lambda x: x[1])
for j in range(1, n):
    sx, sy, si = xy[j - 1]
    tx, ty, ti = xy[j]
    G.append((min(abs(sx - tx), abs(sy - ty)), si, ti))

u = UnionFind(n)
ans = 0
G.sort()
for c, x, y in G:
    if u.root_same(x, y):
        continue
    u.unite(x, y)
    ans += c
print(ans)
