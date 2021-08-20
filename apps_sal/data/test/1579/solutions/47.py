from collections import defaultdict
import sys
input = sys.stdin.readline


def inpl():
    return list(map(int, input().split()))


class UnionFind:

    def __init__(self, N=None):
        if N is None or N < 1:
            self.parent = defaultdict(lambda: -1)
        else:
            self.parent = [-1] * int(N)

    def root(self, n):
        if self.parent[n] < 0:
            return n
        else:
            m = self.root(self.parent[n])
            self.parent[n] = m
            return m

    def merge(self, m, n):
        rm = self.root(m)
        rn = self.root(n)
        if rm != rn:
            if -self.parent[rm] < -self.parent[rn]:
                (rm, rn) = (rn, rm)
            self.parent[rm] += self.parent[rn]
            self.parent[rn] = rm

    def size(self, n):
        return -self.parent[self.root(n)]

    def connected(self, m, n):
        return self.root(m) == self.root(n)

    def groups(self):
        if isinstance(self.parent, list):
            return list(map(lambda x: x < 0, self.parent)).count(True)
        else:
            return list(map(lambda x: x < 0, self.parent.values())).count(True)


class CountUp:

    def __init__(self, start=0):
        self.index = start - 1

    def __call__(self):
        self.index += 1
        return self.index


N = int(input())
uf = UnionFind()
for _ in range(N):
    (x, y) = inpl()
    uf.merge(2 * x + 1, 2 * y)
Ng = uf.groups()
nx = [0] * Ng
ny = [0] * Ng
gi = defaultdict(CountUp())
for k in uf.parent.keys():
    if k % 2:
        nx[gi[uf.root(k)]] += 1
    else:
        ny[gi[uf.root(k)]] += 1
ans = sum([nx[g] * ny[g] for g in range(Ng)]) - N
print(ans)
