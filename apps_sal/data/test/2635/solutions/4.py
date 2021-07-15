class Solution:
     def spiralOrder(self, matrix):
         """
         :type matrix: List[List[int]]
         :rtype: List[int]
         """
         res = []
         if not matrix:
             return res
         
         left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1
         
         while left <= right and top <= bottom:
             res += [matrix[top][i] for i in range(left,right+1)]
             res += [matrix[i][right] for i in range(top+1,bottom)]
             res += [matrix[bottom][i] for i in range(right, left-1,-1) if top < bottom]
             res += [matrix[i][left] for i in range(bottom-1,top,-1) if left < right]
             left+=1
             right-=1
             top+=1
             bottom-=1
         return res
