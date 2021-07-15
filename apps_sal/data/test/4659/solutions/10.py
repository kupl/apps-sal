class Solution:
     def generate(self, numRows):
         """
         :type numRows: int
         :rtype: List[List[int]]
         """
         if numRows == 0:
             return []
         result = [[1]]
         if numRows == 1:
             return result
         result.append([1, 1])
         if numRows == 2:
             return result
         for row in range(2, numRows):
             l, r = 0, 1
             tmp = [1]
             while r < len(result[row-1]):
                 tmp.append(result[row-1][l]+result[row-1][r])
                 l += 1
                 r += 1
             tmp.append(1)
             result.append(tmp)
         return result
