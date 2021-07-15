class Solution:
     def bulbSwitch(self, n):
         """
         :type n: int
         :rtype: int
         """
         cnt = 0
         for i in range(n):
             num = (i+1) ** 2
             if num > n:
                 break
             cnt += 1
         return cnt
