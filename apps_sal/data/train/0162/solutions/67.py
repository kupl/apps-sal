class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # Create dp 2D array
        dp = [[-1] * (len(text2)) for _ in range(len(text1))]

        # Recursive helper function
        def lcsForCell(i, j):
            # Boundary conditions
            if (i < 0) or (j < 0):
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            # If letters are the same
            if text1[i] == text2[j]:
                dp[i][j] = lcsForCell(i-1, j-1) + 1

            else:
                dp[i][j] = max(lcsForCell(i-1, j), lcsForCell(i, j-1))

            return dp[i][j]
        
        return lcsForCell(len(text1)-1, len(text2)-1)
        
                

