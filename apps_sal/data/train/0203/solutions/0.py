class Solution:
     def uniquePaths(self, m, n):
         """
         :type m: int
         :type n: int
         :rtype: int
         """
         def f(n):
             ret = 1
             for i in range(1, n+1):
                 ret *= i
             return ret
         return f(m+n-2)//(f(m-1)*f(n-1))
