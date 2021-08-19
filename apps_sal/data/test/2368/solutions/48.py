from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n + 1
        self.parents = [-1] * self.n

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

        # TODO 根を返す
        return x

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
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.append(0)
    B.append(0)
    uf = UnionFind(N + 1)
    for _ in range(M):
        c, d = list(map(int, input().split()))
        uf.union(c, d)
    A_sums = defaultdict(int)
    B_sums = defaultdict(int)
    for i in range(1, N + 1):
        x = uf.find(i)
        A_sums[x] += A[i - 1]
        B_sums[x] += B[i - 1]
    for a, b in zip(list(A_sums.values()), list(B_sums.values())):
        if a != b:
            print('No')
            return
    print('Yes')


main()
