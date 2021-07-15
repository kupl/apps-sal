class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        
        @lru_cache(maxsize=None)
        def helper(i, j):
            
            if i >= len(text1) or j >= len(text2):
                return 0
            
            elif text1[i] == text2[j]:
                return 1 + helper(i+1, j+1)
            
            l = helper(i + 1, j)
            r = helper(i, j + 1)
            
            return max(l, r)
                
        return helper(0, 0)
                
                

