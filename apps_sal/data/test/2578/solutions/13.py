import sys


class Union_Find:

    def __init__(self, num):
        self.par = [-1] * (num + 1)
        self.size = [1] * (num + 1)

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            x = self.par[x]
            return self.find(x)

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.par[rx] < self.par[ry]:
                self.par[ry] = rx
                self.size[rx] += self.size[ry]
            elif self.par[rx] > self.par[ry]:
                self.par[rx] = ry
                self.size[ry] += self.size[rx]
            else:
                self.par[rx] -= 1
                self.par[ry] = rx
                self.size[rx] += self.size[ry]
        return

    def size_query(self, x):
        return self.size[self.find(x)]


(n, q) = list(map(int, input().split()))
query = [tuple(map(int, sys.stdin.readline().split())) for _ in range(q)]
tree = Union_Find(n)
for a in query:
    k = a[0]
    if k >= 2:
        b = a[1]
        for i in a[2:]:
            tree.union(b, i)
ans = [tree.size_query(tree.find(i + 1)) for i in range(n)]
print(' '.join(map(str, ans)))
