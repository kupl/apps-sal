class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(maxsize = None)
        def memo_solve(index1, index2):
            
            if index1 == len(text1) or index2 == len(text2):
                return 0
            
            if text1[index1] == text2[index2]:
                return 1 + memo_solve(index1 + 1, index2 + 1)
            else:
                return max(memo_solve(index1, index2+1), memo_solve(index1+1, index2))
            
        return memo_solve(0,0)
