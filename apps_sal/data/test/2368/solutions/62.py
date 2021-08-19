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

    def __str__(self):
        return '\n'.join(('{}: {}'.format(r, self.members(r)) for r in self.roots()))


def main():
    (N, M) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if sum(A) != sum(B):
        print('No')
    else:
        f = 0
        uf = UnionFind(N)
        for _ in range(M):
            (C, D) = list(map(int, input().split()))
            C -= 1
            D -= 1
            uf.union(C, D)
        wa = [0 for i in range(N)]
        tle = [0 for i in range(N)]
        for i in range(N):
            wa[uf.find(i)] += A[i]
            tle[uf.find(i)] += B[i]
        if wa == tle:
            print('Yes')
        else:
            print('No')


main()
