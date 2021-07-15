class Solution:
     def generateMatrix(self, n):
         res = [[0 for i in range(n)] for j in range(n)]
         count, rowNum = 1, n
         rowIndex1, rowIndex2, colIndex1, colIndex2 = 0, n - 1, n - 1, 0
 
         while rowNum >= 1:
             for i in range(colIndex2, colIndex1 + 1):
                 res[rowIndex1][i] = count
                 count += 1
             rowIndex1 += 1
 
             for i in range(rowIndex1, rowIndex2 + 1):
                 res[i][colIndex1] = count
                 count += 1
             colIndex1 -= 1
 
             for i in range(colIndex1, colIndex2 - 1, -1):
                 res[rowIndex2][i] = count
                 count += 1
             rowIndex2 -= 1
 
             for i in range(rowIndex2, rowIndex1 - 1, -1):
                 res[i][colIndex2] = count
                 count += 1
             colIndex2 += 1
             rowNum -= 2
         return res

