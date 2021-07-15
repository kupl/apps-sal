class Solution:
     def spiralOrder(self, matrix):
         """
         :type matrix: List[List[int]]
         :rtype: List[int]
         """
         # 0 is right, 1 is down, 2 is left, 3 is up
         state = 0
         next_direction = [1, 2, 3, 0]
         r = []
         
         while len(matrix) > 0:
             if state == 0:
                 r += matrix[0]
                 matrix = matrix[1:]
                 state = next_direction[state]
             elif state == 1:
                 r += [m[len(matrix[0]) - 1] for m in matrix]
                 matrix = [m[:len(matrix[0]) - 1] for m in matrix]
                 state = 2
             elif state == 2:
                 r += reversed(matrix[-1])
                 matrix = matrix[:-1]
                 state = 3
             elif state == 3:
                 r += [matrix[j][0] for j in range(len(matrix) - 1, -1, -1)]
                 matrix = [m[1:] for m in matrix]
                 state = 0
                
             # Covers the case of a list of empty lists (eg. [[],[],[]])
             if len(matrix) >= 1 and not matrix[0]:
                 matrix = []
                 
         return r
         

