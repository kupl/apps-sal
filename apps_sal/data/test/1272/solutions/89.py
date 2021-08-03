import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
AB = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)][::-1]


class UnionFind():
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
            x, y = y, x

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
        return [-x for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())


uf = UnionFind(N)
ans = []
cnt = N * (N - 1) // 2
for a, b in AB:
    ans.append(cnt)
    if uf.same(a, b):
        continue
    cnt -= uf.size(a) * uf.size(b)
    uf.union(a, b)
for a in ans[::-1]:
    print(a)
