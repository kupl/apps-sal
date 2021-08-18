import collections
import itertools


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def check(b):
            h = {}
            w = ''
            for i, v in enumerate(b):
                w += s[i]
                if v == 0:
                    if w in h:
                        return -1
                    else:
                        h[w] = 1
                    w = ''
            w += s[-1]
            if w != '':
                if w in h:
                    return -1
                else:
                    h[w] = 1
            return len(h)
        ans = 1
        for b in itertools.product([0, 1], repeat=len(s) - 1):
            n = check(b)
            if n > 0:
                ans = max(ans, n)
        return ans
