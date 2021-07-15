class Solution:
     def myPow(self, x, n):
         """
         :type x: float
         :type n: int
         :rtype: float
         """
         if n < 0:
             return 1 / self.powRecu(x, -n)
         
         return self.powRecu(x, n)
     
     def powRecu(self, x, n):
         if n == 0:
             return 1.0
         
         if n % 2 == 0:
             return self.powRecu(x * x, n // 2)
         else:
             return x * self.powRecu(x * x, n // 2)
