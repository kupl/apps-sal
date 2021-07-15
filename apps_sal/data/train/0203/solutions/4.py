class Solution:
     def uniquePaths(self, m, n):
         """
         :type m: int
         :type n: int
         :rtype: int
         """
         num_paths = [[0 for _ in range(n)] for _ in range(m)]
         for i in range(m):
             for j in range(n):
                 above = num_paths[i-1][j] if i > 0 else 0
                 left = num_paths[i][j-1] if j > 0 else 0
                 num_paths[i][j] = above + left
                 if i==0 and j==0:
                     num_paths[0][0] = 1
         return num_paths[m-1][n-1]

