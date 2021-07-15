class Solution:
     def uniquePaths(self, m, n):
         """
         :type m: int
         :type n: int
         :rtype: int
         """
         all=m-1+n-1
         x=1
         y=1
         for i in range(m-1):
             x=x*(all-i)
             y=y*(i+1)
         return x//y
             

