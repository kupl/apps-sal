class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * (n)

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

    def issame(self, x, y):
        return self.find[x] == self.find(y)


'''
参考
https://qiita.com/K_SIO/items/03ff1fc1184cb39674aa
'''


def __starting_point():
    N, M = list(map(int, input().split()))
    uf = UnionFind(N)

    for _ in range(M):
        A, B = list(map(int, input().split()))
        uf.union(A - 1, B - 1)

    ans = 0

    for i in range(N):
        ans = max(ans, uf.size(i))

    print(ans)


__starting_point()
