from collections import Counter


class UnionFind:

    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, i: int) -> None:
        if self.parent[i] == i:
            return i
        else:
            return self.find(self.parent[i])

    def unite(self, i: int, j: int) -> None:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return
        if self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        else:
            self.parent[root_j] = root_i
            if self.rank[root_i] == self.rank[root_j]:
                self.rank[root_i] += 1

                
N, K, L = map(int, input().split())

uf1 = UnionFind(N)
for _ in range(K):
    i, j = map(int, input().split())
    uf1.unite(i - 1, j - 1)

uf2 = UnionFind(N)
for _ in range(L):
    i, j = map(int, input().split())
    uf2.unite(i - 1, j - 1)

set_id_pairs = [(uf1.find(i), uf2.find(i)) for i in range(N)]
counter = Counter(set_id_pairs)
counts = [counter[set_id_pairs[i]] for i in range(N)]
print(' '.join(str(c) for c in counts))
