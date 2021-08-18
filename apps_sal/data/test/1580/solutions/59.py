import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline


def geta(fn=lambda s: s.decode()):
    return list(map(fn, readline().split()))


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


class UnionFind:

    def __init__(self, N: int):
        self.d = [-1 for _ in range(N)]

    def root(self, x: int) -> int:
        if self.d[x] < 0:
            return x
        self.d[x] = self.root(self.d[x])
        return self.d[x]

    def unite(self, x: int, y: int) -> bool:
        x, y = self.root(x), self.root(y)
        if x == y:
            return False
        if self.d[x] > self.d[y]:
            x, y = y, x
        self.d[x] += self.d[y]
        self.d[y] = x
        return True

    def same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def size(self, x: int):
        return -self.d[self.root(x)]

    def show(self):
        m = {}
        for n in range(len(self.d)):
            r = self.root(n)

            if r not in m:
                m[r] = [n]
            else:
                m[r].append(n)

        print("root -> childs")
        print("---------------------")
        for key in m:
            print(("{} -> {}".format(key, m[key])))


def main():
    n, m = geta(int)

    uf = UnionFind(2 * n)

    ans = n

    for _ in range(m):
        x, y, z = geta(int)

        united = False
        if z & 1 == 0:
            united = uf.unite(2 * x - 2, 2 * y - 2) and uf.unite(2 * x - 1, 2 * y - 1)
        else:
            united = uf.unite(2 * x - 2, 2 * y - 1) and uf.unite(2 * x - 1, 2 * y - 2)

        if united:
            ans -= 1

    print(ans)


def __starting_point():
    main()


__starting_point()
