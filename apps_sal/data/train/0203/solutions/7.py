class Solution:
     import math
     def uniquePaths(self, m, n):
         """
         :type m: int
         :type n: int
         :rtype: int
         """
         if m==1 or n==1:
             return 1
         r,c = m-1, n-1
         return int(math.factorial(r+c)/(math.factorial(r)*math.factorial(c)))

