class Solution:
     def spiralOrder(self, matrix):
         """
         :type matrix: List[List[int]]
         :rtype: List[int]
         """
         
         m = len(matrix)
         if m == 0:
             return []
         n = len(matrix[0])
     
 
         visit = set()
         result = []
 
         pos = [0, 0]
         visit.add(tuple(pos))
         result.append(matrix[pos[0]][pos[1]])
 
         while len(visit) < m*n:
 
             for i in range(pos[1]+1, n):
                 
                 if (pos[0], i) in visit:
                     break
                 pos[1] = i
                 visit.add(tuple(pos))
                 result.append(matrix[pos[0]][pos[1]])
 
 
             for i in range(pos[0]+1, m):
                 
                 if (i, pos[1]) in visit:
                     break
                 pos[0] = i
                 visit.add(tuple(pos))
                 result.append(matrix[pos[0]][pos[1]])
 
             for i in range(pos[1]-1, -1, -1):
                 
                 if (pos[0], i) in visit:
                     break
 
                 pos[1] = i
                 visit.add(tuple(pos))
                 result.append(matrix[pos[0]][pos[1]])
 
             for i in range(pos[0]-1, -1, -1):
 
                 if (i, pos[1]) in visit:
                     break
 
                 pos[0] = i
                 
                 visit.add(tuple(pos))
                 result.append(matrix[pos[0]][pos[1]])
                 
         return result
                 
         return result
             

