class Solution:
     import sys
     def divide(self, dividend, divisor):
         """
         :type dividend: int
         :type divisor: int
         :rtype: int
         """
         maxint = 2**31 - 1
         minint = -2**31
         sign = (2*(dividend>0) - 1) * (2*(divisor>0) - 1)
         quotient = 0
         dividend *= (2*(dividend>0) - 1)
         divisor *= (2*(divisor>0) - 1)
         remainder = dividend
         for i in reversed(list(range(32))):
             if remainder == 0: break
             if divisor << i <= remainder:
                 remainder -= divisor << i
                 quotient += 1 << i
         quotient *= sign
         print(quotient)
         if quotient > maxint or quotient < minint:  quotient = maxint
         return quotient
