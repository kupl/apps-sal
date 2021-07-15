class Solution:
     def getRow(self, rowIndex):
         """
         :type rowIndex: int
         :rtype: List[int]
         """
         if rowIndex < 0:
             return list()
         if rowIndex == 0:
             return list([1])
         l = list([1])
         for i in range(1,rowIndex+1):
             pre_value = l[0] #1
             for j in range(1,i):#j = 3
                 temp = l[j] #1
                 l[j] = pre_value+l[j] #4
                 pre_value = temp #1
             l.append(1)
         return l
                 
             

