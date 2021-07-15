class Solution:
     def searchMatrix(self, matrix, target):
         """
         :type matrix: List[List[int]]
         :type target: int
         :rtype: bool
         """
         def get(now, n):
             x = now//n
             y = now%n
             return matrix[x][y]
             
         m = len(matrix)
         if m == 0:
             return False
         n = len(matrix[0])
         if n == 0:
             return False
         
         i = 0
         j = m * n - 1
         while(i <= j):
             mid = (i + j)//2
             if get(mid, n) == target:
                 return True
             elif get(mid, n) < target:
                 i = mid + 1
             else:
                 j = mid - 1
         return False
     

