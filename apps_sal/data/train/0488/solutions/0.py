class Solution:
     def kthSmallest(self, matrix, k):
         """
         :type matrix: List[List[int]]
         :type k: int
         :rtype: int
         """
         arr = []
         for i in matrix:
             for j in i:
                 arr.append(j)
         arr.sort()
         print(arr)
         return arr[k-1]
