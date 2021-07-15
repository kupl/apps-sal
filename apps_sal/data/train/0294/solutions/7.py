class Solution:
     def totalNQueens(self, n):
         """
         :type n: int
         :rtype: int
         """
         def dfs(cols, diag_45, diag_135, depth=0):
             nonlocal result
             row = len(cols)
             if row == n:
                 result += 1
                 return 
             for col in range(n):
                 if col not in cols and (row - col) not in diag_45 and (row + col) not in diag_135:
                     dfs(cols + [col], diag_45 + [row - col], diag_135 + [row + col], depth + 1)
 
         result = 0
         dfs([], [], [])
         return result
