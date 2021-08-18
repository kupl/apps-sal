class UFS:
    def __init__(self, N):
        self._parent = list(range(N))

    def find(self, x):
        if self._parent[x] != x:
            self._parent[x] = self.find(self._parent[x])
        return self._parent[x]

    def union(self, x, y):
        xroot, yroot = self.find(x), self.find(y)
        if xroot != yroot:
            self._parent[xroot] = yroot


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:

        def primeFactors(k):
            out = set()
            while k % 2 == 0:
                out.add(2)
                k //= 2
            for i in range(3, int(math.sqrt(k)) + 1, 2):
                while k % i == 0:
                    out.add(i)
                    k //= i
            if k > 2:
                out.add(k)
            return out

        n = len(A)
        maxa = max(A)

        ufs = UFS(maxa + 1)

        for cur in A:
            factors = primeFactors(cur)

            for f in factors:
                ufs.union(f, cur)

        count = [0] * (maxa + 1)
        for cur in A:
            count[ufs.find(cur)] += 1

        return max(count)
