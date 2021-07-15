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

N, M = list(map(int, input().split()))
uf = UnionFind(N)
ab_list = []
ans =0
for i in range(M):
    a,b = list(map(int, input().split()))
    a, b = a-1, b-1
    ab_list.append([a, b])

ans_list = [0 for i in range(M)]
for i in range(M, 0, -1):
    if i == M:
        ans_list[i-1] = N*(N-1)//2
    else:
        if uf.find(ab_list[i][0]) != uf.find(ab_list[i][1]):
            ans_list[i-1] = ans_list[i] - uf.size(ab_list[i][0])*uf.size(ab_list[i][1])
        else:
            ans_list[i-1] = ans_list[i]
        uf.union(ab_list[i][0], ab_list[i][1])
print((*ans_list))

