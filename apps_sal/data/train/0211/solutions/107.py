from functools import lru_cache
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        @lru_cache(None)
        def rec(i, fs):
            if i == len(s):
                return 0
            ans = float('-inf')
            sub = ''
            for j in range(i, len(s)):
                sub += s[j]
                if sub not in fs:
                    ans = max(ans, rec(j+1, fs | frozenset([sub])) + 1)
            return ans
        return rec(0, frozenset())
