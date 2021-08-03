from math import ceil, sqrt
from typing import List


class Solution:
    MAXN = 100001
    spf = [0 for i in range(MAXN)]

    def largestComponentSize(self, A: List[int]) -> int:
        spf = self.spf
        MAXN = self.MAXN

        def sieve():
            spf[1] = 1
            for i in range(2, MAXN):
                spf[i] = i
            for i in range(4, MAXN, 2):
                spf[i] = 2

            for i in range(3, ceil(sqrt(MAXN))):
                if spf[i] == i:
                    for j in range(i * i, MAXN, i):
                        if spf[j] == j:
                            spf[j] = i

        def getFactorization(x):
            ret = []
            while x != 1:
                if not ret or spf[x] != ret[-1]:
                    ret.append(spf[x])
                x = x // spf[x]

            return ret

        sieve()
        parents = {0: [0, 0]}

        def find(curr):
            if curr == parents[curr][0]:
                return curr
            return find(parents[curr][0])

        for i in range(len(A)):
            factors = getFactorization(A[i])
            parent = 0
            for f in factors:
                parents.setdefault(f, [f, 0])
                p = find(f)
                if parent != 0 and p != parent:
                    parents[parent][1] += parents[p][1]
                    parents[p][0] = parent
                    parents[p][1] = 0
                else:
                    parent = p

            parents[parent][1] += 1
        return max(list(parents.values()), key=lambda x: x[1])[1]
