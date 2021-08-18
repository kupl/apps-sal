import collections
import itertools


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def check(b):
            h = {}
            w = ''
            b = list(b) + [0]
            for i, v in enumerate(b):
                w += s[i]
                if v == 0:
                    if w in h:
                        return -1
                    h[w] = 1
                    w = ''
            return len(h)
        ans = 1
        for b in itertools.product([0, 1], repeat=len(s) - 1):
            n = check(b)
            ans = max(ans, n)
        return ans
