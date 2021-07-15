class Solution:
     def spiralOrder(self, matrix):
         """
         :type matrix: List[List[int]]
         :rtype: List[int]
         """
         #O(n^2) time; O(1) space
         if not matrix:
             return []
         
         ans = []
         rowSize = len(matrix); colSize = len(matrix[0])       
         rowStart=0; colStart=0; rowEnd = rowSize-1; colEnd = colSize-1        
         
         while rowStart <= rowEnd and colStart <= colEnd:
             
             for colIndex in range(colStart,colEnd+1):
                 ans.append(matrix[rowStart][colIndex])
             rowStart += 1;
             
             for rowIndex in range(rowStart,rowEnd+1):
                 ans.append(matrix[rowIndex][colEnd])
             colEnd -= 1;
             
             if rowStart > rowEnd or colStart > colEnd: break                
             
             for colIndex in range(colEnd,colStart-1,-1):
                 ans.append(matrix[rowEnd][colIndex])
             rowEnd -= 1;                           
                 
             for rowIndex in range(rowEnd,rowStart-1,-1):
                 ans.append(matrix[rowIndex][colStart])
             colStart += 1;                                     
             
         return ans

