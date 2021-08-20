class UnionFind(object):

    def __init__(self, n, recursion=False):
        self._par = list(range(n))
        self._size = [1] * n
        self._recursion = recursion

    def root(self, k):
        if self._recursion:
            if k == self._par[k]:
                return k
            self._par[k] = self.root(self._par[k])
            return self._par[k]
        else:
            root = k
            while root != self._par[root]:
                root = self._par[root]
            while k != root:
                (k, self._par[k]) = (self._par[k], root)
            return root

    def unite(self, i, j):
        (i, j) = (self.root(i), self.root(j))
        if i == j:
            return False
        if self._size[i] < self._size[j]:
            (i, j) = (j, i)
        self._par[j] = i
        self._size[i] += self._size[j]
        return True

    def is_connected(self, i, j):
        return self.root(i) == self.root(j)

    def size(self, k):
        return self._size[self.root(k)]


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        M = max(A)
        primes = []
        sieve = list(range(M + 1))
        for i in range(2, M + 1):
            if sieve[i] == i:
                primes.append(i)
            for p in primes:
                if i * p > M or sieve[i] < p:
                    break
                sieve[i * p] = p
        uf = UnionFind(n)
        color = [-1] * (M + 1)
        for (i, a) in enumerate(A):
            while a != 1:
                p = sieve[a]
                if color[p] != -1:
                    uf.unite(i, color[p])
                else:
                    color[p] = i
                a //= p
        return max((uf.size(i) for i in range(n)))
