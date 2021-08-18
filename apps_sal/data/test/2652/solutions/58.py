import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


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
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.parents[self.find(x)]


def kruskal(max_node, edge):
    """
    :param max_node: UnionFind木に渡す頂点数です
    :param edge: edge = [(コスト, 頂点1, 頂点2),...]の形で重み付き隣接リストを渡して下さい
    :return: 最小全域木のコストの和
    """
    edge.sort()
    uf = UnionFind(max_node)
    cost_sum = 0
    for cost, node1, node2 in edge:
        if not uf.same(node1, node2):
            cost_sum += cost
            uf.union(node1, node2)
    return cost_sum


def resolve():
    n = int(input())
    X, Y = [], []
    for i in range(n):
        x, y = list(map(int, input().split()))
        X.append([x, i])
        Y.append([y, i])

    X.sort()
    Y.sort()
    cost = []
    for i in range(n - 1):
        cost.append([abs(X[i][0] - X[i + 1][0]), X[i][1], X[i + 1][1]])
        cost.append([abs(Y[i][0] - Y[i + 1][0]), Y[i][1], Y[i + 1][1]])

    res = kruskal(n, cost)
    print(res)


def __starting_point():
    resolve()


__starting_point()
