# python program to do this question using disjoint set technique
import math


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        parent = [-1] * (100001)

        def find(val, parent):
            if parent[val] == -1:
                return val
            parent[val] = find(parent[val], parent)
            return parent[val]

        def union(x, y, parent):
            xp = find(x, parent)
            yp = find(y, parent)
            if xp != yp:
                parent[yp] = xp

        for val in A:
            for i in range(2, int(math.sqrt(val)) + 1):
                if val % i == 0:
                    union(i, val, parent)
                    union(val, val // i, parent)

        c = 0
        mp = {}
        for val in A:
            pval = find(val, parent)
            c = max(c, 1 + mp.get(pval, 0))
            mp[pval] = mp.get(pval, 0) + 1

        return c
