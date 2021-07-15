import bisect
import collections
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline
ACMOD = 1000000007
INF = 1 << 60


def lmi():
    return list(map(int, input().split()))


def llmi(n):
    return [lmi() for _ in range(n)]


N, M = lmi()
ABC = llmi(M)


class BellmanFord:
    def __init__(self, n, start=0):
        self.n = n
        self.cost = [INF] * n
        self.cost[start] = 0
        self.edge = dict()

    def add_edge(self, _from, _to, _cost):
        self.edge[(_from, _to)] = _cost

    def fill_cost(self, check=False):
        negative_loops = set()
        for i in range(self.n):
            for (_from, _to), _cost in list(self.edge.items()):
                if self.cost[_from] != INF and self.cost[_to] > self.cost[_from] + _cost:
                    self.cost[_to] = self.cost[_from] + _cost
                    if check:
                        negative_loops.add(_to)
        return negative_loops


bf = BellmanFord(N)
for a, b, c in ABC:
    bf.add_edge(a - 1, b - 1, -c)
bf.fill_cost()
negative_loops = bf.fill_cost(check=True)
# print(negative_loops, bf.cost)
if N - 1 in negative_loops:
    print('inf')
else:
    print((-bf.cost[-1]))

