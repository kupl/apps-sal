from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        prefix = [0] * n
        suffix = [0] * n
        pset = set()
        sset = set()
        ans = 0
        for i in range(0, n):
            l = s[i]
            r = s[n - i - 1]
            pset.add(l)
            sset.add(r)
            prefix[i] = len(pset)
            suffix[n - 1 - i] = len(sset)

        for i in range(0, n - 1):
            if prefix[i] == suffix[i + 1]:
                ans = ans + 1
        return ans
