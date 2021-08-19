class UnionFind:

    def __init__(self, N):
        self.parents = [i for i in range(N)]
        self.sizes = [1 for _ in range(N)]

    def root(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.sizes[x] < self.sizes[y]:
            (x, y) = (y, x)
        self.sizes[x] += self.sizes[y]
        self.parents[y] = x
        return True

    def size(self, x):
        return self.sizes[self.root(x)]


(N, M) = map(int, input().split())
tree = UnionFind(N)
AB = []
for _ in range(M):
    (a, b) = map(int, input().split())
    AB.append([a, b])
AB = AB[::-1]
tree = UnionFind(N)
ans = [N * (N - 1) // 2]
for i in range(M):
    (a, b) = AB[i]
    (a, b) = (tree.root(a - 1), tree.root(b - 1))
    if a != b:
        ans.append(ans[-1] - tree.size(a) * tree.size(b))
    else:
        ans.append(ans[-1])
    tree.unite(a, b)
ans = ans[:M][::-1]
for i in range(M):
    print(ans[i])
