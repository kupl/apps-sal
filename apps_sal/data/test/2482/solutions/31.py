import sys

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


N, K, L = map(int,input().split())
uf_road = UnionFind(N)
uf_train = UnionFind(N)

for i in range(K):
    p,q = map(int,input().split())
    p -= 1
    q -= 1
    uf_road.union(p,q)

for i in range(L):
    p,q = map(int,input().split())
    p -= 1
    q -= 1
    uf_train.union(p,q)

pair_list = []
for i in range(N):
    pair_list.append((uf_road.find(i), uf_train.find(i), i))

pair_list.sort()
ans = [0] * N

pair = (pair_list[0][0], pair_list[0][1])
countup_list = [pair_list[0][2]]
for i in range(1,N):
    if pair == (pair_list[i][0], pair_list[i][1]):
        countup_list.append(pair_list[i][2])
    else:
        for c in countup_list:
            ans[c] += len(countup_list)
        pair = (pair_list[i][0], pair_list[i][1])
        countup_list = [pair_list[i][2]]

for c in countup_list:
    ans[c] += len(countup_list)
    
for i in range(N):
    print(ans[i], end=" ")
