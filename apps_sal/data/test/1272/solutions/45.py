import math


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


n_nodes, n_path = list(map(int, input().split()))
paths = [[0, 0] for _ in range(n_path)]
for i in range(n_path):
    a, b = list(map(int, input().split()))
    paths[i] = [a - 1, b - 1]


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
        '''
        xとyは-=1して使う
        '''
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


now_ans = combinations_count(n_nodes, 2)
paths = paths[::-1]
uf = UnionFind(n_nodes)
ans_ls = [0] * (n_path)
ans_ls[-1] = now_ans
for i, path in enumerate(paths[:-1]):
    a, b = path
    if not uf.same(a, b):
        now_ans -= uf.size(a) * uf.size(b)
        uf.union(a, b)
    ans_ls[-2 - i] = now_ans
for ans in ans_ls:
    print(ans)
