class Solution:
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # Make a grid of 0's with len(text2) + 1 columns 
        # and len(text1) + 1 rows.
        dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        # Iterate up each column, starting from the last one.
        for col in reversed(list(range(len(text2)))):
            for row in reversed(list(range(len(text1)))):
                # If the corresponding characters for this cell are the same...
                if text2[col] == text1[row]:
                    dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
                # Otherwise they must be different...
                else:
                    dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])
        
        # The original problem's answer is in dp_grid[0][0]. Return it.
        return dp_grid[0][0]
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp_grid = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for col in reversed(list(range(len(B)))):
            for row in reversed(list(range(len(A)))):
                if B[col] == A[row]:
                    dp_grid[row][col] = 1 + dp_grid[row+1][col+1]
                else:
                    dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])
        return dp_grid[0][0]
                
        

