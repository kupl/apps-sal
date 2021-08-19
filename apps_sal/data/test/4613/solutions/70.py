class UnionFind:  # 引数は頂点の数、1インデックス
    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    # 検索
    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.parents[x] = y
        else:
            self.parents[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)


def __starting_point():
    N, M = list(map(int, input().split()))
    bridges = [tuple(map(int, input().split())) for _ in range(M)]

    count = 0
    for i in range(M):
        union_find = UnionFind(N)
        for j in range(M):
            if i == j:
                continue
            a, b = bridges[j]
            union_find.union(a, b)

        for j in range(1, N):
            if union_find.find(j) != union_find.find(j + 1):
                count += 1
                break

    print(count)


__starting_point()
