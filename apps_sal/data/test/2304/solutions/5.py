import sys
readline = sys.stdin.readline


class WeightedUnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n
        # 根への距離を管理
        self.weight = [0] * n

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            y = self.find(self.parents[x])
            # 親への重みを追加しながら根まで走査
            self.weight[x] += self.weight[self.parents[x]]
            self.parents[x] = y
            return y

    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        # xの木の高さ < yの木の高さ
        if self.rank[rx] < self.rank[ry]:
            self.parents[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        # xの木の高さ ≧ yの木の高さ
        else:
            self.parents[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            # 木の高さが同じだった場合の処理
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    # xからyへのコスト
    def diff(self, x, y):
        return self.weight[x] - self.weight[y]


def main():
    N, M = map(int, readline().rstrip().split())
    uf = WeightedUnionFind(N)

    for _ in range(M):
        l, r, d = map(int, readline().rstrip().split())
        l -= 1
        r -= 1
        if uf.same(l, r):
            if uf.diff(l, r) != d:
                print('No')
                return

        uf.union(l, r, d)

    print('Yes')


def __starting_point():
    main()


__starting_point()
