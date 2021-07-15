import sys
sys.setrecursionlimit(10**7)


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1]*n

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

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


n, m = list(map(int, input().split()))
ab=[list(map(int, input().split())) for _ in range(m)]

uf = UnionFind(n)
tmp_ans = n*(n-1)//2
ans = []
for i in range(m):
    ans.append(tmp_ans)
    a=ab[m-1-i][0]
    b=ab[m-1-i][1]
    a-=1
    b-=1
    if not uf.is_same(a,b):
        tmp_ans-=uf.size(a)*uf.size(b)
    uf.union(a,b)

ans.reverse()
for i in ans:
    print(i)

