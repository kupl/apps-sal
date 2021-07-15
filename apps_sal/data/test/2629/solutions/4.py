class Solution:
     def generateMatrix(self, n):
         matrix = []
         if n == 0:
             return matrix
 
         matrix = [[0]*n for i in range(n)]
         rowBegin = 0
         rowEnd = n - 1
         colBegin = 0
         colEnd = n - 1
         num = 0
 
         while True:
             # traverse right
             for j in range(colBegin, colEnd+1):
                 num += 1
                 matrix[rowBegin][j] = num
             rowBegin += 1
             if rowBegin > rowEnd:
                 break
                 
             # traverse down
             for j in range(rowBegin, rowEnd+1):
                 num += 1
                 matrix[j][colEnd] = num
             colEnd -= 1
             if colBegin > colEnd:
                 break
                 
             # traverse left
             for j in range(colEnd, colBegin-1, -1):
                 num += 1
                 matrix[rowEnd][j] = num
             rowEnd -= 1
             if rowBegin > rowEnd:
                 break
                 
             # traverse up
             for j in range(rowEnd, rowBegin-1, -1):
                 num += 1
                 matrix[j][colBegin] = num
             colBegin += 1
             if colBegin > colEnd:
                 break
         return matrix
