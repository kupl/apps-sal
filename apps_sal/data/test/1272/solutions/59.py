class UnionFind:
    def __init__(self, n):
        self.nodes = n
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n
        self.rank = [0] * n

    def find(self, i):  # どの集合に属しているか（根ノードの番号）
        if self.parents[i] == i:
            return i
        else:
            self.parents[i] = self.find(self.parents[i])  # 経路圧縮
            return self.parents[i]

    def unite(self, i, j):  # 二つの集合を併合
        pi = self.find(i)
        pj = self.find(j)
        if pi != pj:
            if self.rank[pi] < self.rank[pj]:
                self.sizes[pj] += self.sizes[pi]
                self.parents[pi] = pj
            else:
                self.sizes[pi] += self.sizes[pj]
                self.parents[pj] = pi
                if self.rank[pi] == self.rank[pj]:
                    self.rank[pi] += 1

    def same(self, i, j):  # 同じ集合に属するかを判定
        return self.find(i) == self.find(j)

    def get_parents(self):  # 根ノードの一覧を取得
        for n in range(self.nodes):  # findで経路圧縮する
            self.find(n)
        return self.parents

    def size(self, i):
        p = self.find(i)
        return self.sizes[p]


N, M = map(int, input().split())
AB = []
B = []
for m in range(M):
    a, b = map(int, input().split())
    AB.append((a - 1, b - 1))

ans = []
score = N * (N - 1) // 2
uf = UnionFind(N)
for a, b in AB[::-1]:
    ans.append(score)
    if not uf.same(a, b):
        score -= uf.size(a) * uf.size(b)
        uf.unite(a, b)

for score in ans[::-1]:
    print(score)
