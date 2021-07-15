class Solution:
     def spiralOrder(self, matrix):
         """
         :type matrix: List[List[int]]
         :rtype: List[int]
         """
         if len(matrix) == 0:
             return []
         if len(matrix) == 1:
             return matrix[0]
         if len(matrix[0]) == 1:
             result = []
             for m in matrix:
                 result.append(m[0])
             return result
         
         
         boxTop = -1
         boxRight = len(matrix[0])
         boxLeft = -1
         boxBottom = len(matrix)
         
         
         count = 0
         direction = [0, 1]
         ptr = [0, 0]
         predict = [0, 0]
         result = []
         
         while count < len(matrix) * len(matrix[0]):
             count += 1
             result.append(matrix[ptr[0]][ptr[1]])
             ptr[0] += direction[0]
             ptr[1] += direction[1]
             
             predict[0] = ptr[0] + direction[0]
             predict[1] = ptr[1] + direction[1]
             
             
             if direction == [0, 1] and predict[1] >= boxRight:
                 direction = [1, 0]
                 boxTop += 1
             elif direction == [1,0] and predict[0] >= boxBottom:
                 direction = [0, -1]
                 boxRight -= 1
             elif direction == [0, -1] and predict[1] <= boxLeft:
                 direction = [-1, 0]
                 boxBottom -= 1
             elif direction == [-1, 0] and predict[0] <= boxTop:
                 direction = [0, 1]
                 boxLeft += 1
             
         return result
