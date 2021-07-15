class Solution:
     """
     def minmum(self, triangle, i, j):
         if (i + 1) == len(triangle):
             return triangle[i][j]
         return min(self.minmum(triangle, i+1, j), self.minmum(triangle, i+1, j+1)) + triangle[i][j]
     """
     
     def minimumTotal(self, triangle):
         """
         :type triangle: List[List[int]]
         :rtype: int
         """
         #return self.minmum(triangle, 0, 0)
         
         rows = len(triangle)
         minPath = triangle[rows-1]
         for i in range(rows-1)[::-1]:
             for j in range(i+1):
                 minPath[j] = min(minPath[j], minPath[j+1]) + triangle[i][j]
         return minPath[0]
         

