class Solution:
     def maximalRectangle(self, matrix):
         """
         :type matrix: List[List[str]]
         :rtype: int
         """
         if not matrix:
             return 0
         m = len(matrix)
         n = len(matrix[0])
         ans = 0
         heights = [0]*(n+1)
 
         for i in range(m):
             for j in range(n):
                 heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
             stack = [-1]
             for i in range(n + 1):
                 while heights[i] < heights[stack[-1]]:
                     h = heights[stack.pop()]
                     w = i - stack[-1] - 1
                     ans = max(ans, w*h)
                 stack.append(i)
         return ans
                 

