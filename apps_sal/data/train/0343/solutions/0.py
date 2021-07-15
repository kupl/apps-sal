class Solution:
     def numSquares(self, n):
         """
         :type n: int
         :rtype: int
         """
         while(n%4 == 0):
             n = n/4
         if n%8 == 7: return 4;
         a = int(0)
         while(a*a <= n):
             b = int(math.sqrt(n-a*a))
             if (a*a+b*b == n):
                 print('a=',a,'b+',b)
                 return (not not a) + (not not b)
             a += 1
         return 3
