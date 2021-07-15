# 辺を消していく操作は難しい
# 操作を逆から考え、辺を足していくと考える
#####################


class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, v):  # vが属する集合の根を返す
        if self.parents[v] < 0:
            return v
        else:
            self.parents[v] = self.find(self.parents[v])
            return self.parents[v]

    def unite(self, u, v):  # 「uが属する集合」と「vが属する集合」を併合（根同士を結ぶ）
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return

        if self.parents[u] > self.parents[v]:  # u < v に統一する
            u, v = v, u

        self.parents[u] += self.parents[v]
        self.parents[v] = u

    def size(self, v):  # vが属する集合の要素数
        return -self.parents[self.find(v)]

    def same(self, u, v):  # uとvが同じ集合に属するか否か
        return self.find(u) == self.find(v)
############################################
N, M = list(map(int, input().split()))
uf = UnionFind(N)
edges = []

for i in range(M):
    A, B = list(map(int, input().split()))
    # 0-indexに直す
    edges.append((A - 1, B - 1))

# n_C_2 = N*(N-1)//2
# [辺が(M-1)本(=1本崩落), ..., 辺が1本(=M-1本崩落), 辺が0本(=M本崩落)]
# [-1]はn_C_2のまま、[-2]から[-M]に向かって逆順に更新していく（辺を増やしていく）

total = [N * (N - 1) // 2 for _ in range(M)]

# -i-1 = -1,-2,...,-(M-1)
# -i-2 = -2,-3,...,-M
for i in range(M - 1):
    u, v = edges[-i - 1]
    # 既に同じ集合に属しているなら、辺を足しても、行き来出来ない組み合わせ数は変わらない（減らない）
    if uf.same(u, v):
        total[-i - 2] = total[-i - 1]
    # uとvが異なる集合に属している場合
    # 辺を張ることで、ダメな組み合わせが(uの要素数)*(vの要素数)だけ減る　（行き来できるようになる）
    else:
        total[-i - 2] = total[-i - 1] - uf.size(u) * uf.size(v)
        uf.unite(u, v)

for t in total:
    print(t)

