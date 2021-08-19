class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        from itertools import combinations
        L = list(range(1, n))
        for d in range(n - 1, 0, -1):
            for x in combinations(L, d):
                hh = [0] + list(x) + [n]
                tmep = [s[hh[j]:hh[j + 1]] for j in range(len(hh) - 1)]
                if len(set(tmep)) == len(tmep):
                    return d + 1
        return 1
