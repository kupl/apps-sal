class Solution:
     def uniquePaths(self, m, n):
         """
         :type m: int
         :type n: int
         :rtype: int
         """
         M = [[1 for _ in range(n)] for _ in range(2)]
         for i in range(m-1, -1, -1):
             for j in range(n-1, -1, -1):
                 if i == m-1 or j == n-1: continue
                 else: M[i%2][j] = M[(i+1)%2][j] + M[i%2][j+1]
         return M[0][0]
