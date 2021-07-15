class Solution:
     def kthSmallest(self, matrix, k):
         """
         :type matrix: List[List[int]]
         :type k: int
         :rtype: int
         """
         from heapq import heappush, heappop
         n = len(matrix[0])
         heap = []
         for i in range(n):
             heappush(heap, (matrix[0][i], 0, i))
         for _ in range(k-1):
             v, x, y= heappop(heap)
             if x == n - 1:
                 continue
             heappush(heap, (matrix[x+1][y], x+1, y))
         return heappop(heap)[0]
