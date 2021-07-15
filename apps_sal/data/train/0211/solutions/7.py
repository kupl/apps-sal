class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        
        
        def rec(i, myset):
            if i == len(s):
                return 0
            ans = -float('inf')
            for j in range(i, len(s)):
                if s[i:j + 1] not in myset:
                    ans = max(ans, 1 + rec(j + 1, myset | set([s[i:j + 1]])))
            return ans
        return rec(0, set())
