class Solution:
     def searchMatrix(self, matrix, target):
         """
         :type matrix: List[List[int]]
         :type target: int
         :rtype: bool
         """
         if not matrix:
             return False
         row_size = len(matrix)
         column_size = len(matrix[0])
         
         low = 0
         high = row_size * column_size - 1
         
         while low <= high: 
             mid = (high + low) // 2
             r, c = divmod(mid, column_size)
             val = matrix[r][c]
             if target == val:
                 return True
             elif target > val:
                 low = mid + 1
             else:
                 high = mid - 1
         
         return False
