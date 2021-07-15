class Solution:
     def spiralOrder(self, matrix):
         """
         :type matrix: List[List[int]]
         :rtype: List[int]
         """
         ans = []
         
         if len(matrix) is 0:
             return ans
         
         import numpy as np
         npa = np.array(matrix, dtype = int)
         
         r_s = c_s = 0
         r_e = len(matrix)
         c_e = len(matrix[0])
         
         go_row = True
         forward = True
         row_index = r_s
         col_index = c_e - 1
         
         while(r_s < r_e and c_s < c_e):
             if go_row:
                 # Traverse row
                 s = npa[row_index,c_s:c_e].tolist()
                 if forward:
                     r_s += 1
                     row_index = r_e -1
                 else:
                     r_e -= 1
                     row_index = r_s
                     s.reverse()
                 ans.extend(s)
                 
                 
             else:
                 # traverse col
                 s = npa[r_s:r_e, col_index].tolist()
                 if forward:
                     c_e -= 1
                     col_index = c_s
                 else:
                     c_s += 1
                     col_index = c_e - 1
                     s.reverse()
                 ans.extend(s)
                 forward = not forward
                                 
             go_row = not go_row
         
         return ans
