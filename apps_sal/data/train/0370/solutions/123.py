class DSU:
    def __init__(self, size):
        self.indexes = {i: i for i in range(size)}
        self.sizes = {i: 1 for i in range(size)}

    def root(self, i):
        node = i
        while i != self.indexes[i]:
            i = self.indexes[i]

        while node != i:
            nnode = self.indexes[node]
            self.indexes[node] = i
            node = nnode
        return i

    def unite(self, i, j):
        ri, rj = self.root(i), self.root(j)
        if ri == rj:
            return
        else:
            self.indexes[rj] = ri
            self.sizes[ri] += self.sizes[rj]


class Solution:
    def primeSet(self, n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return self.primeSet(n // i) | set([i])
        return set([n])

    def largestComponentSize(self, A: List[int]) -> int:

        d = collections.defaultdict(list)
        for i in range(len(A)):
            s = self.primeSet(A[i])
            for v in s:
                d[v].append(i)

        dsu = DSU(len(A))
        for k in d:
            for ind in d[k][1:]:
                dsu.unite(d[k][0], ind)

        ans = 1
        for i in range(len(A)):
            ans = max(ans, dsu.sizes[i])

        return ans
