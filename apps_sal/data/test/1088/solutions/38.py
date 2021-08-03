from collections import defaultdict
import math


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


N, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]

c_pattern = list()  # swapable なcの組み合わせ数
r_pattern = list()  # swapable なrの組み合わせ数

for c1 in range(N):
    for c2 in range(c1 + 1, N):
        ok = True
        for i in range(N):
            if a[i][c1] + a[i][c2] > K:
                ok = False
                break
        if ok:
            c_pattern.append([c1, c2])


for r1 in range(N):
    for r2 in range(r1 + 1, N):
        ok = True
        for i in range(N):
            if a[r1][i] + a[r2][i] > K:
                ok = False
                break
        if ok:
            r_pattern.append([r1, r2])


def total_pattern(pattern_list):
    uf = UnionFind(N)
    for p in pattern_list:
        uf.union(p[0], p[1])
    ans = 1
    # print(uf.roots())
    for r in uf.roots():
        ans *= math.factorial(uf.size(r))

    return ans


print(total_pattern(c_pattern) * total_pattern(r_pattern) % 998244353)
