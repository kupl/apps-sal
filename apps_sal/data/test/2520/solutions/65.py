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

    def __str__(self):
        return '\n'.join(('{}: {}'.format(r, self.members(r)) for r in self.roots()))


(N, M, K) = map(int, input().split())
tree = UnionFind(N)
not_friend_candidates = []
for i in range(M):
    (A, B) = list(map(int, input().split()))
    A -= 1
    B -= 1
    tree.union(A, B)
    not_friend_candidates.append([A, B])
for j in range(K):
    (C, D) = list(map(int, input().split()))
    C -= 1
    D -= 1
    not_friend_candidates.append([C, D])
ans = [0] * N
for (i, j) in not_friend_candidates:
    if tree.same(i, j):
        ans[i] -= 1
        ans[j] -= 1
for i in range(N):
    ans[i] += tree.size(i) - 1
print(*ans)
