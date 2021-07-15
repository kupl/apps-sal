class Solution:
     def grayCode(self, n):
         """
         :type n: int
         :rtype: List[int]
         """
         if n == 0:
             return [0]
     
         q = [0, -1]
     
         for i in range(n):
             tag = 0
             while q[0] != -1:
                 item = q.pop(0)
                 q.append(item * 2 + tag)
                 q.append(item * 2 + (1 - tag))
                 tag = 1 - tag
             q.pop(0)
             q.append(-1)
     
         q.pop(-1)
         
         return q
