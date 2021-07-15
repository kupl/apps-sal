from functools import lru_cache

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        N = len(s)
        
        @lru_cache(None)
        def numChanges(i, j):
            ct = 0
            while i < j:
                if s[i] != s[j]:
                    ct += 1
                i += 1
                j -= 1
            return ct
        
        @lru_cache(None)
        def dp(i, k):
            if i < k - 1:
                return inf
            if k == 1:
                return numChanges(0, i)
            return min(dp(j-1, k-1) + numChanges(j, i) for j in range(1, i+1))
        
        return dp(N-1, k)
