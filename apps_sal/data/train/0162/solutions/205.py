class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo = [[None for i in range(len(text2)+1)] for _ in range(len(text1)+1)]
        def rec(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            
            if text1[i] == text2[j]:
                if not memo[i+1][j+1]:
                    memo[i+1][j+1] = rec(i+1, j+1)
                return 1 + memo[i+1][j+1]
            else:
                if not memo[i][j+1]:
                    memo[i][j+1] = rec(i, j+1)
                if not memo[i+1][j]:
                    memo[i+1][j] = rec(i+1, j)
                return max(memo[i][j+1], memo[i+1][j])
            
        return rec(0, 0)
