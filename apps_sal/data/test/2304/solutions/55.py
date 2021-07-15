import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


class WeightedUnionFind:
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.parents = [-1] * n_nodes

        # 親への重みを管理
        self.weights = [0] * n_nodes

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            parent = self.find(self.parents[x])
            self.weights[x] += self.weights[self.parents[x]]
            self.parents[x] = parent
            return parent

    # xからyへの重みがw
    def unite(self, x, y, w):
        w += self.weights[x]
        w -= self.weights[y]
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x
            w *= -1

        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.weights[y] = w
        return

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return -self.parents[self.find(x)]

    def get_weight(self, x, y):
        return self.weights[y] - self.weights[x]


def main():
    N, M = list(map(int, input().split()))
    tree = WeightedUnionFind(N)
    for _ in range(M):
        L, R, D = list(map(int, input().split()))
        L -= 1
        R -= 1

        if tree.is_same(L, R):
            if tree.get_weight(L, R) == D:
                continue
            else:
                print("No")
                return
        else:
            tree.unite(L, R, D)

    print("Yes")
    return


def __starting_point():
    main()

__starting_point()
