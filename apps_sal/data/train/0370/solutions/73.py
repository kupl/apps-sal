class UnionFind:

    def __init__(self, A):
        self._arr = {v: -1 for v in A}

    def union(self, u, v):
        p1 = self.find(u)
        p2 = self.find(v)
        if p1 != p2:
            self._arr[p1] = p2
            return True
        return False

    def find(self, u):
        if self._arr.get(u, -1) == -1:
            return u
        self._arr[u] = self.find(self._arr[u])
        return self._arr[u]


class Solution:

    def factorsOf(self, n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n = n // 2
        for i in range(3, int(sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.add(i)
                n = n // i
        if n > 2:
            factors.add(n)
        return factors

    def largestComponentSize(self, A: List[int]) -> int:
        dsu = UnionFind(A)
        for n in A:
            for factor in self.factorsOf(n):
                dsu.union(n, factor)
        cnt_map = collections.Counter()
        ans = 0
        for v in A:
            p = dsu.find(v)
            cnt_map[p] += 1
            ans = max(cnt_map[p], ans)
        return ans
