import collections
import itertools
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def check(b):
            h = {}
            w = ''
            b = list(b) + [0] # b[len(s)-1] should be zero
            for i, v in enumerate(b):
                w += s[i]
                if v == 0:
                    if w in h: return -1
                    h[w] = 1
                    w = ''
            return len(h)
        ans = 1
        for b in itertools.product([0,1], repeat=len(s)-1):
            # if b[i]==1, b[i] is concatenated to b[i+1]
            n = check(b)
            ans = max(ans, n)
        return ans
