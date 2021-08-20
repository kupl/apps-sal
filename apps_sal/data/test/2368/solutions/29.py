import collections
import itertools
import operator


class UnionFind:

    def __init__(self, elems=None):

        class KeyDict(dict):

            def __missing__(self, key):
                self[key] = key
                return key
        self.parent = KeyDict()
        self.rank = collections.defaultdict(int)
        if elems is not None:
            for elem in elems:
                (_, _) = (self.parent[elem], self.rank[elem])

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def are_same(self, x, y):
        return self.find(x) == self.find(y)

    def grouper(self):
        roots = [(x, self.find(x_par)) for (x, x_par) in self.parent.items()]
        root = operator.itemgetter(1)
        for (_, group) in itertools.groupby(sorted(roots, key=root), root):
            yield [x for (x, _) in group]


(N, M) = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
uf = UnionFind()
for m in range(M):
    (n1, n2) = list(map(int, input().split()))
    uf.unite(n1, n2)
for n in range(N):
    n = n + 1
    uf.unite(n, n)
ans = 'Yes'
for g_nodes in list(uf.grouper()):
    a_sum = 0
    b_sum = 0
    for node in g_nodes:
        a_sum += A[node - 1]
        b_sum += B[node - 1]
    if a_sum != b_sum:
        ans = 'No'
print(ans)
