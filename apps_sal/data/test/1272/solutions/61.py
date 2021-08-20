import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


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

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for (i, x) in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())


def main():
    (N, M, *AB) = map(int, read().split())
    AB = list(reversed(AB[2:]))
    count = N * (N - 1) // 2
    ans = [count]
    uf = UnionFind(N)
    for (a, b) in zip(AB[::2], AB[1::2]):
        a -= 1
        b -= 1
        if not uf.same(a, b):
            count -= uf.size(a) * uf.size(b)
            uf.union(a, b)
        ans.append(count)
    print('\n'.join(map(str, reversed(ans))), sep='\n')
    return


def __starting_point():
    main()


__starting_point()
