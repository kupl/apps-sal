class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(maxsize=None)
        def helper(i1, i2):
            if i1 == len(text1) or i2 == len(text2):
                return 0
            else:
                if text1[i1] == text2[i2]:
                    return helper(i1+1,i2+1) + 1
                return max(helper(i1+1,i2), helper(i1,i2+1))
        
        return helper(0, 0)
