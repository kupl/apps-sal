import sys
input = lambda: sys.stdin.readline().rstrip()
 

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
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())




n,m = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))

u = UnionFind(n)
for i in range(m):
    c,d = list(map(int,input().split()))
    c -= 1
    d -= 1
    u.union(c,d)

a_pa = [0 for i in range(n)]
b_pa = [0 for i in range(n)]
for i in range(n):
    a_pa[u.find(i)] += a[i]
    b_pa[u.find(i)] += b[i]


if a_pa == b_pa:
    print("Yes")
else:
    print("No")


