class Solution:
     def grayCode(self, n):
         """
         :type n: int
         :rtype: List[int]
         """
         result = [0]
         for i in range(n):
             temp = [] 
             for num in result:
                 temp.append(num + 2**i)
             result += temp[::-1]
             
         return result

