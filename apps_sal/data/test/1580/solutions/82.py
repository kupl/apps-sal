class UnionFind:
    """
    size の要素数の UnionFind を管理する
    data 中の負数の要素が根となる
    """

    def __init__(self, size):
        # 根は子を含む集合のデータ数を負数でもつ
        self.data = [-1] * size

    def merge(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False

        # y の方がデータ数を多く
        if self.data[x] < self.data[y]:
            x, y = y, x

        # y に x をつなげる
        self.data[y] += self.data[x]
        self.data[x] = y
        return True

    def root(self, x):
        if self.data[x] < 0:
            return x
        self.data[x] = self.root(self.data[x])
        return self.data[x]

    def size(self, x):
        """
        根は負数でデータ数を管理しているのでそれを返す
        """
        return -self.data[self.root(x)]


def main():
    N, M = [int(_) for _ in input().split()]
    uf = UnionFind(N)
    for i in range(M):
        x, y, z = [int(_) for _ in input().split()]
        uf.merge(x - 1, y - 1)

    cnt = 0
    for i in range(N):
        if uf.root(i) == i:
            cnt += 1
    print(cnt)


def __starting_point():
    main()


__starting_point()
