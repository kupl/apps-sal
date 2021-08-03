from collections import Counter


class UnionFind:
    # n個の要素を初期化
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.rank = [0] * n

    # 木の根を求める
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # xとyの属する集合を併合
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # xとyが同じ集合に属するか判定
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # 要素xが属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]


N, K, L = map(int, input().split())
roads = [list(map(int, input().split())) for i in range(K)]
trains = [list(map(int, input().split())) for i in range(L)]

uf_road = UnionFind(N)
uf_train = UnionFind(N)

for road in roads:
    x, y = road
    uf_road.unite(x - 1, y - 1)

for train in trains:
    x, y = train
    uf_train.unite(x - 1, y - 1)

pairs = []
for i in range(N):
    pairs.append((uf_road.find(i), uf_train.find(i)))

cnt = Counter(pairs)

ans = [cnt[pair] for pair in pairs]
print(*ans)
