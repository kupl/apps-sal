class UnionFind:
    from typing import List, Set

    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n

    def merge(self, x, y) -> int:
        x = self.leader(x)
        y = self.leader(y)
        if x == y:
            return 0
        if self.parent[x] > self.parent[y]:
            (x, y) = (y, x)
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return self.parent[x]

    def same(self, x, y) -> bool:
        return self.leader(x) == self.leader(y)

    def leader(self, x) -> int:
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.leader(self.parent[x])
            return self.parent[x]

    def size(self, x) -> int:
        return -self.parent[self.leader(x)]

    def groups(self) -> List[Set[int]]:
        groups = dict()
        for i in range(self.n):
            p = self.leader(i)
            if not groups.get(p):
                groups[p] = set()
            groups[p].add(i)
        return list(groups.values())


(n, m) = map(int, input().split())
uf = UnionFind(n)
for i in range(m):
    (a, b) = map(int, input().split())
    uf.merge(a - 1, b - 1)
grp = uf.groups()
ans = 0
for i in range(len(grp)):
    if len(grp[i]) > ans:
        ans = len(grp[i])
print(ans)
