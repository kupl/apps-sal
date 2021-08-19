class UnionFind:

    def __init__(self, n):
        self.parents = [-1] * n

    def find_root(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find_root(self.parents[x])
        return self.parents[x]

    def unite(self, x, y):
        root_x = self.find_root(x)
        root_y = self.find_root(y)
        if root_x == root_y:
            return
        if self.parents[root_x] > self.parents[root_y]:
            (root_x, root_y) = (root_y, root_x)
        self.parents[root_x] += self.parents[root_y]
        self.parents[root_y] = root_x

    def are_in_same(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def get_size(self, x):
        return -self.parents[self.find_root(x)]

    def get_roots(self):
        roots = set()
        for (i, x) in enumerate(self.parents):
            if x < 0:
                roots.add(i)
        return roots

    def count_roots(self):
        return len(self.get_roots())


(N, M) = list(map(int, input().split()))
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
graph = UnionFind(N)
for i in range(M):
    (c, d) = list(map(int, input().split()))
    graph.unite(c - 1, d - 1)
(sum_a, sum_b) = ([0] * N, [0] * N)
for i in range(N):
    r = graph.find_root(i)
    sum_a[r] += a[i]
    sum_b[r] += b[i]
judge = 'Yes'
for r in graph.get_roots():
    if sum_a[r] != sum_b[r]:
        judge = 'No'
        break
print(judge)
