class Solution:
     def myPow(self, x, n):
         """
         :type x: float
         :type n: int
         :rtype: float
         """
         if 0 <= n < 2:
             return [1, x][n]
         if n < 0:
             n, x = -n, 1 / x
         temp = divmod(n, 2)
         return self.myPow(x, temp[0]) ** 2 * self.myPow(x, temp[1])
