from copy import deepcopy as copy
from operator import itemgetter


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * (n + 1)  # それぞれの要素がどの要素の子であるか

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]  # それぞれの要素の根を再帰的に求める

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)  # x,yが同じ集合に属するかどうか

    def size(self, x):
        return -self.par[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if root == self.find(i)]


def main():
    n = int(input())
    bridge = [None] * n
    for i in range(n):
        bridge[i] = [int(x) for x in input().split()] + [i]

    judge = []

    bridge.sort()
    for i in range(n - 1):
        judge.append((bridge[i + 1][0] - bridge[i][0], bridge[i][2], bridge[i + 1][2]))

    bridge.sort(key=itemgetter(1))
    for i in range(n - 1):
        judge.append((bridge[i + 1][1] - bridge[i][1], bridge[i][2], bridge[i + 1][2]))

    judge.sort()
    union = UnionFind(n)
    count = 0
    cost = 0
    for k in range(2 * n):
        c, i, j = judge[k]
        if union.same(i, j):
            continue
        union.union(i, j)
        cost += c
        count += 1
        if count == n - 1:
            break

    print(cost)


def __starting_point():
    main()


__starting_point()
