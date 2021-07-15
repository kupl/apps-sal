MOD = 998244353

N, K = list(map(int, input().split()))
AMat = [list(map(int, input().split())) for _ in range(N)]

class UnionFind:
    def __init__(self, N):
        self.parent = list(range(N))
        self.rank = [0] * N
        self.size = [1] * N

    def find(self, x):
        if self.parent[x]==x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.size[y] += self.size[x]
        else:
            self.parent[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]

uf_x = UnionFind(N)
for i in range(N-1):
    for j in range(i+1, N):
        flag = True
        for y in range(N):
            if AMat[y][i] + AMat[y][j] > K:
                flag = False
                break
        if flag:
            uf_x.unite(i, j)

uf_y = UnionFind(N)
for i in range(N-1):
    for j in range(i+1, N):
        flag = True
        for x in range(N):
            if AMat[i][x] + AMat[j][x] > K:
                flag = False
                break
        if flag:
            uf_y.unite(i, j)

ans_list1 = [0] * N
for i in range(N):
    ans_list1[uf_x.find(i)] += 1

ans_list2 = [0] * N
for i in range(N):
    ans_list2[uf_y.find(i)] += 1

ans_list = ans_list1 + ans_list2
ans = 1
for a in ans_list:
    if a >= 1:
        for x in range(1, a+1):
            ans *= x
            ans %= MOD

print((ans%MOD))

