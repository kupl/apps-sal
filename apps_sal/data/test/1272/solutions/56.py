import sys


class UnionFind:
    def __init__(self, n):
        self.table = [-1] * n

    def _root(self, x):
        stack = []
        tbl = self.table
        while tbl[x] >= 0:
            stack.append(x)
            x = tbl[x]
        for y in stack:
            tbl[y] = x
        return x

    def find(self, x, y):
        return self._root(x) == self._root(y)

    def union(self, x, y):
        r1 = self._root(x)
        r2 = self._root(y)
        if r1 == r2:
            return
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            self.table[r1] += d2
        else:
            self.table[r1] = r2
            self.table[r2] += d1


def main():
    n, m = list(map(int, sys.stdin.buffer.readline().split()))
    uf = UnionFind(n)
    ans = [n*(n-1)//2]
    for x in reversed(sys.stdin.buffer.readlines()):
        a, b = list(map(int, x.split()))
        a -= 1
        b -= 1
        if uf.find(a, b):
            ans.append(ans[-1])
            continue
        ba, bb = uf.table[uf._root(a)], uf.table[uf._root(b)]
        ans.append(ans[-1] - ba*bb)
        uf.union(a, b)
    ans.reverse()
    print(("\n".join(map(str, ans[1:]))))


def __starting_point():
    main()

__starting_point()
