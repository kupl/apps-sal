from collections import defaultdict


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
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


def fact(n, mod=998244353):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
        ans %= mod
    return ans


mod = 998244353

n, k = map(int, input().split())
lst = [[int(i) for i in input().split()] for _ in range(n)]

ans = 1
un1 = UnionFind(n)
for i in range(n - 1):
    for j in range(i + 1, n):
        flag = True
        for l in range(n):
            if lst[i][l] + lst[j][l] > k:
                flag = False
                break
        if flag:
            un1.union(i, j)
for i in range(n):
    if i == un1.find(i):
        num = un1.size(i)
        ans *= fact(num)
        ans %= mod

un2 = UnionFind(n)
for i in range(n - 1):
    for j in range(i + 1, n):
        flag = True
        for l in range(n):
            if lst[l][i] + lst[l][j] > k:
                flag = False
                break
        if flag:
            un2.union(i, j)
for i in range(n):
    if i == un2.find(i):
        num = un2.size(i)
        ans *= fact(num)
        ans %= mod
print(ans)
