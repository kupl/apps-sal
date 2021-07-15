class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memo = [[0 for _ in range(m)] for _ in range(n)]
        res = 0
        for row in range(n):
            if row == 0 and text2[row] == text1[0]:
                memo[row][0] = 1
            else:
                memo[row][0] = memo[row-1][0]
            
                if text2[row] == text1[0]:
                    memo[row][0] = 1
       
        
        for col in range(m):
            if col == 0 and text1[col] == text2[0]:
                memo[0][col] = 1
            else:
                memo[0][col] = memo[0][col-1]
            
                if text1[col] == text2[0]:
                    memo[0][col] = 1
        print(memo)
        for row in range(1, n):
            for col in range(1, m):
                if text1[col] != text2[row]:
                    memo[row][col] = max(memo[row-1][col],
                                         memo[row][col-1],
                                         memo[row-1][col-1])
                else:
                    memo[row][col] = 1 + min(memo[row-1][col],
                                         memo[row][col-1],
                                         memo[row-1][col-1])
        
        return memo[-1][-1]
                
        

