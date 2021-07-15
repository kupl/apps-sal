class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        
        @lru_cache(None)
        def helper(i, j):
            if i == len(s1) or j == len(s2):
                return 0
            if s1[i] == s2[j]:
                return 1 + helper(i + 1, j + 1)
            else:
                return max(helper(i+1, j), helper(i, j + 1))
        return helper(0,0)

