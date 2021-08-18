from sys import stdin, setrecursionlimit
from operator import itemgetter

setrecursionlimit(10 ** 9)
INF = 1 << 60


def input():
    return stdin.readline().strip()


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


N = int(input())
P = [0] * N
for i in range(N):
    x, y = list(map(int, input().split()))
    P[i] = (i, x, y)

edges = []
for i in (1, 2):
    P.sort(key=itemgetter(i))
    for j in range(N - 1):
        edges.append((P[j][0], P[j + 1][0], P[j + 1][i] - P[j][i]))

edges.sort(key=itemgetter(2))
uf = UnionFind(N)
ans = 0
cities = 1
for i, j, c in edges:
    if not uf.same(i, j):
        uf.union(i, j)
        ans += c
        cities += 1
        if cities == N:
            break

print(ans)
