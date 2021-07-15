import sys
readline = sys.stdin.readline
from collections import Counter

class UnionFind():
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

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def main():
    N, K, L = map(int, readline().rstrip().split())
    uf_road = UnionFind(N)
    uf_train = UnionFind(N)
    
    for _ in range(K):
        p, q = map(int, readline().rstrip().split())
        uf_road.union(p-1, q-1)
    
    for _ in range(L):
        r, s = map(int, readline().rstrip().split())
        uf_train.union(r-1, s-1)
    
    pairs = []
    for i in range(N):
        pairs.append((uf_road.find(i), uf_train.find(i)))
    
    cnt = Counter(pairs)
    res = [cnt[pair] for pair in pairs]
    print(*res)

def __starting_point():
    main()
__starting_point()
