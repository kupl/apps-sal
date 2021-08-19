import sys
from collections import defaultdict


class UnionFind:

    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.root[x] == x:
            return x
        else:
            y = self.find(self.root[x])
            self.root[x] = y
            return self.root[x]

    def unite(self, x, y):
        if self.is_same(x, y):
            return
        rx = self.find(x)
        ry = self.find(y)
        if self.rank[rx] < self.rank[ry]:
            self.root[rx] = ry
        else:
            self.root[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def is_same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    input = sys.stdin.readline
    V = 10 ** 5
    N = int(input())
    uft = UnionFind(2 * V)
    for _ in range(N):
        (x, y) = list(map(int, input().split()))
        x -= 1
        y += V - 1
        uft.unite(x, y)
    cnt_x = defaultdict(lambda: 0)
    cnt_y = defaultdict(lambda: 0)
    for i in range(2 * V):
        root = uft.find(i)
        if i < V:
            cnt_x[root] += 1
        else:
            cnt_y[root] += 1
    ans = 0
    for root in list(cnt_x.keys()):
        ans += cnt_x[root] * cnt_y[root]
    return ans - N


def __starting_point():
    print(main())


__starting_point()
