class UnionFind:

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
            (x, y) = (y, x)
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    (n, m) = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(m)]
    uf = UnionFind(n)
    ans = [n * (n - 1) // 2]
    for (a, b) in ab[::-1]:
        (sa, sb) = (uf.size(a - 1), uf.size(b - 1))
        if uf.same(a - 1, b - 1):
            ans.append(ans[-1])
        else:
            ans.append(ans[-1] - sa * sb)
        uf.union(a - 1, b - 1)
    for i in range(1, m + 1):
        print(ans[-(i + 1)])


main()
