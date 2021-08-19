class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * (n + 1)

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
            (x, y) = (y, x)
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
        return [i for (i, x) in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}


(N, M) = map(int, input().split())
Union = UnionFind(N)
bad_value = N * (N - 1) // 2
bridge = []
for i in range(M):
    (a, b) = map(int, input().split())
    bridge.append((a, b))
bridge.reverse()
ans = [bad_value]
for (a, b) in bridge:
    if Union.same(a, b):
        Union.union(a, b)
        ans.append(bad_value)
        continue
    else:
        X = Union.size(a)
        Y = Union.size(b)
        Union.union(a, b)
        bad_value -= X * Y
        ans.append(bad_value)
        continue
ans.reverse()
for i in range(1, M + 1):
    print(ans[i])
