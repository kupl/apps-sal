class Solution:
     def getRow(self, rowIndex):
         """
         :type rowIndex: int
         :rtype: List[int]
         """
         out = [1]
         for i in range(1,rowIndex+1):
             temp = []
             for j in range(0, i-1):
                 temp.append(out[j]+out[j+1])
             out = [1]+temp+[1]
         return out
