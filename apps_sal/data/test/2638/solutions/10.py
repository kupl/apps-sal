class Solution:
     def minimumTotal(self, triangle):
         import math
         """
         :type triangle: List[List[int]]
         :rtype: int
         """
         cost = {(-1, -1): math.inf, (-1,0):0, (-1, 1):math.inf}
         for i in range(len(triangle)):
             cost[(i, -1)] = math.inf
             cost[i, len(triangle[i])] = math.inf
 
         for i in range(len(triangle)):
             for j in range(len(triangle[i])):
                 cost[(i, j)] = triangle[i][j] + min(cost[(i-1, j)], cost[(i-1, j-1)])
                 
         return min([cost[(len(triangle)-1, j)] for j in range(len(triangle[-1]))])
