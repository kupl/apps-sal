from collections import Counter


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


N, K, L = list(map(int, input().split()))
pq = [list(map(int, input().split())) for i in range(K)]
rs = [list(map(int, input().split())) for i in range(L)]

uf_road = UnionFind(N)
uf_train = UnionFind(N)

for i in range(K):
    uf_road.union(pq[i][0] - 1, pq[i][1] - 1)
for i in range(L):
    uf_train.union(rs[i][0] - 1, rs[i][1] - 1)

# 各都市に連結しているroadとtrainの積集合の探索はTLE
# ans = []
# for i in range(N):
#   ans.append(len(set(uf_road.members(i)) & set(uf_train.members(i))))
# print(*ans)

# road,trainの根のペアで同じペアを持つ都市は連結している
pair = [(uf_road.find(i), uf_train.find(i)) for i in range(N)]
ans = Counter(pair)
print(*[ans[i] for i in pair])
