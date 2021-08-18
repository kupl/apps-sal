
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

    def size(self, x):
        return -self.parents[self.find(x)]

    def is_same(self, x, y):
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


def resolve():
    N, M, K = list(map(int, input().split()))
    uf = UnionFind(N)
    sub_friend = [1] * N

    frind = [[] for _ in range(N)]
    for _ in range(M):
        a, b = [int(x) - 1 for x in input().split()]
        frind[a].append(b)
        frind[b].append(a)
        sub_friend[a] += 1
        sub_friend[b] += 1

    block = [[] for _ in range(N)]
    for _ in range(K):
        c, d = [int(x) - 1 for x in input().split()]
        block[c].append(d)
        block[d].append(c)

    for i in range(N):
        for to in frind[i]:
            uf.union(i, to)

    ans = [uf.size(i) - sub_friend[i] for i in range(N)]

    for i in range(N):
        for bl in block[i]:
            if uf.is_same(i, bl):
                ans[i] -= 1
    print((*ans))


def __starting_point():
    resolve()


__starting_point()
