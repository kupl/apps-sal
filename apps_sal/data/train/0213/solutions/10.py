class Solution:
     def myPow(self, x, n):
         """
         :type x: float
         :type n: int
         :rtype: float
         """
         output=1
         power=0
         power_applied=1
         product=x
         m=abs(n)
         while m!=0 and power!=m:
             if (power+power_applied*2)<m:
                 product=product*product
                 power_applied=power_applied*2
                 power=power+power_applied
             else:
                 product=x
                 power_applied=1
                 power=power+power_applied
             output=output*product
         if n<0: output=1/output
         return output
