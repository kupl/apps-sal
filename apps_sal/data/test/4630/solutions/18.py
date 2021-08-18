import math
import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)


def getN():
    return int(input())


def getList():
    return list(map(int, input().split()))


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same_check(self, x, y):
        return self.find(x) == self.find(y)


def solve():
    n = getN()
    nums = getList()
    uf = UnionFind(n)
    for i, num in enumerate(nums):
        uf.par[i + 1] = uf.find(i + 1)
        uf.par[num] = uf.find(num)
        if not uf.same_check(i + 1, num):
            uf.union(i + 1, num)

    for i in range(n + 1):
        uf.find(i)
    ans = []
    for i in range(n):
        ans.append(uf.size[uf.par[i + 1]])
    print(*ans)


def main():
    q = getN()
    for _ in range(q):
        solve()


def __starting_point():
    main()


"""
1
3
2 3 1
"""
__starting_point()
