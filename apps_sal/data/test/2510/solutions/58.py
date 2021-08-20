class UnionFind:

    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n + 1)
        self.rnk = [0] * (n + 1)

    def Find_Root(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]

    def Unite(self, x, y):
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        if x == y:
            return
        elif self.rnk[x] > self.rnk[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1

    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    def Count(self, x):
        return -self.root[self.Find_Root(x)]


def main():
    (n, m) = list(map(int, input().split()))
    uf = UnionFind(n)
    for i in range(m):
        (a, b) = list(map(int, input().split()))
        uf.Unite(a, b)
    for i in range(n):
        i += 1
        uf.isSameGroup(i, i)
    ans = 0
    for i in range(n):
        ans = max(ans, -uf.root[i + 1])
    print(ans)


main()
