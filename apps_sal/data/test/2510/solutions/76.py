class UnionFind():  # 0インデックス
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


def __starting_point():
    n, m = list(map(int, input().split()))
    unionFind = UnionFind(n)
    for _ in range(m):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        unionFind.union(a, b)

    value = 0
    for i in range(n):
        value = max(value, unionFind.size(i))

    print(value)


__starting_point()
