import sys
YES = 'Yes'
NO = 'No'


def solve(N: int, M: int, L: 'List[int]', R: 'List[int]', D: 'List[int]'):
    uf = UnionFind(N + 1)
    try:
        for (l, r, d) in zip(L, R, D):
            uf.merge(l, r, d)
        return YES
    except MergeError:
        return NO


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    M = int(next(tokens))
    L = [int()] * M
    R = [int()] * M
    D = [int()] * M
    for i in range(M):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
        D[i] = int(next(tokens))
    print(solve(N, M, L, R, D))


class MergeError(Exception):
    pass


class UnionFind:

    def __init__(self, size: int):
        self.par = list(range(size))
        self.rank = [0] * size
        self.diff_weight = [0] * size

    def root(self, x: int):
        if self.par[x] == x:
            return x
        r = self.root(self.par[x])
        self.diff_weight[x] += self.diff_weight[self.par[x]]
        self.par[x] = r
        return r

    def weight(self, x: int):
        self.root(x)
        return self.diff_weight[x]

    def same(self, x: int, y: int):
        return self.root(x) == self.root(y)

    def merge(self, x: int, y: int, w: int):
        adjusted_w = w + self.weight(x) - self.weight(y)
        x = self.root(x)
        y = self.root(y)
        if x == y:
            if adjusted_w != 0:
                raise MergeError
            return
        if self.rank[x] < self.rank[y]:
            (x, y, adjusted_w) = (y, x, -adjusted_w)
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.par[y] = x
        self.diff_weight[y] = adjusted_w


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
