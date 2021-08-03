import collections
from math import sqrt


class Solution:

    def fac(self, m, a):
        while m[a] != a:
            m[a] = m[m[a]]
            a = m[a]
        return a

    def union(self, m, a, b):
        if m[a] == m[b]:
            return
        pa = self.fac(m, a)
        pb = self.fac(m, b)
        m[pa] = pb

    def largestComponentSize(self, A: List[int]) -> int:
        ma = max(A) + 1
        m = list(range(ma))
        for a in A:
            for k in range(2, int(sqrt(a)) + 1):
                if a % k == 0:
                    self.union(m, a, k)
                    self.union(m, a, a // k)

        count = collections.defaultdict(int)
        for a in A:
            if a != 1:
                count[self.fac(m, a)] += 1

        return max(count.values())
