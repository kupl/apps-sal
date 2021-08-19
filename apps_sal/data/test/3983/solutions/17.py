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

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for (i, x) in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join(('{}: {}'.format(r, self.members(r)) for r in self.roots()))


for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    if n % 2 == 1:
        for _ in range(m):
            _ = input()
        if (n * (n - 1) // 2 - m) % 2 == 1:
            print('First')
        else:
            print('Second')
    else:
        UF = UnionFind(n)
        for _ in range(m):
            (a, b) = list(map(int, input().split()))
            a -= 1
            b -= 1
            UF.union(a, b)
        v1 = UF.size(0)
        vn = UF.size(n - 1)
        if (v1 - vn) % 2 == 1:
            print('First')
        elif (n * (n - 1) // 2 - m - v1) % 2 == 1:
            print('First')
        else:
            print('Second')
