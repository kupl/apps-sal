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
             result.extend(result[::-1])
             #offset = 0 
             start = len(result) // 2
             for i in range(start, len(result)):
                 #if i > 0 and i % cnt == 0:
                 #    offset = cnt;
                 #result[i] += offset 
                 result[i] += cnt
             
         return result
