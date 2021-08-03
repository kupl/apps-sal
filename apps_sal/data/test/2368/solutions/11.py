
class UnionFind:

    def __init__(self, n: int):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unit(self, x: int, y: int):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if self.rank[parent_x] < self.rank[parent_y]:
            self.parent[parent_x] = parent_y
        else:
            self.parent[parent_y] = parent_x
            if self.rank[parent_y] == self.rank[parent_x]:
                self.rank[parent_x] += 1

    def same_check(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


N, M = list(map(int, input().split()))

Als = list(map(int, input().split()))
Bls = list(map(int, input().split()))

uf = UnionFind(N)

for i in range(M):
    c, d = list(map(int, input().split()))
    uf.unit(c, d)

after_als = [0] * N
after_bls = [0] * N
for i in range(N):
    after_als[uf.find(i + 1) - 1] += Als[i]
    after_bls[uf.find(i + 1) - 1] += Bls[i]

for i in range(N):
    if after_als[i] != after_bls[i]:
        print('No')
        return

print('Yes')
