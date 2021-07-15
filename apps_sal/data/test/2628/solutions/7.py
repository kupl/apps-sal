class Solution:
     def grayCode(self, n):
         """
         :type n: int
         :rtype: List[int]
         """
               
         result = [0, 1]
         if n <= 1:
             return result[:n+1]
         res_len = 2 ** n
         
         cnt = 1
         while len(result) != res_len:
             cnt *= 2
             #orig_len = len(result)
             for i in range(cnt - 1, -1, -1):
                 result.append(result[i] + cnt)
             
         return result
