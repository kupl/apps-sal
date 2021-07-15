class Solution:
     def kthSmallest(self, matrix, k):
         """
         :type matrix: List[List[int]]
         :type k: int
         :rtype: int
         """
         
         list = matrix[0]
         
         for i in range(1, len(matrix)):
             list.extend(matrix[i])
             
         list.sort()
         
         return list[k-1]
