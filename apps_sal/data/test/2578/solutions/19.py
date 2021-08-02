import sys
input = sys.stdin.readline


class Union_Find():
    def __init__(self, num):
        self.par = [-1] * (num + 1)
        self.siz = [1] * (num + 1)

    def same_checker(self, x, y):
        return self.find(x) == self.find(y)

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
                self.siz[rx] += self.siz[ry]
            elif self.par[rx] > self.par[ry]:
                self.par[rx] = ry
                self.siz[ry] += self.siz[rx]
            else:
                self.par[rx] -= 1
                self.par[ry] = rx
                self.siz[rx] += self.siz[ry]
        return

    def size(self, x):
        return self.siz[self.find(x)]


n, q = map(int, input().split())
union_find_tree = Union_Find(n)
for i in range(q):
    a = list(map(int, input().split()))
    k = a[0]
    if k >= 2:
        for i in range(2, k + 1):
            union_find_tree.union(a[1], a[i])
ans = []
for i in range(1, n + 1):
    ans.append(union_find_tree.size(i))
print(" ".join(map(str, ans)))
