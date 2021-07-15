class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def solve(i, j):
            # Base case: reached end of one of the strings
            if i == n or j == m:
                return 0
            
            # Memoization case
            if memo[i][j] != -1:
                return memo[i][j]
            
            # Recursive case 1: text1[i] == text2[j]
            if text1[i] == text2[j]:
                memo[i][j] = 1 + solve(i+1, j+1)
                
            # Recursive case 2: text1[i] != text2[j]
            else:
                memo[i][j] = max(solve(i, j+1), solve(i+1, j))
            
            return memo[i][j]
        
        n, m = len(text1), len(text2)
        
        memo = [[-1 for _ in range(m)] for _ in range(n)]
        
        return solve(0, 0)
            

