class Solution:
     def divide(self, dividend, divisor):
         """
         :type dividend: int
         :type divisor: int
         :rtype: int
         """
         MIN_INT = -2**31
         MAX_INT = -MIN_INT - 1
         if divisor == 0 or (dividend == MIN_INT and divisor==-1):
             return MAX_INT
         sign = 1
         if dividend < 0:
             sign = -sign
             dividend = -dividend
         if divisor < 0:
             sign = -sign
             divisor = -divisor
         ans = bits = 0
         while (divisor<<(bits+1)) <= dividend:
             bits += 1
         while bits >= 0:
             if dividend >= (divisor<<bits):
                 dividend -= (divisor<<bits)
                 ans += (1<<bits)
             bits -= 1
         return ans if sign==1 else -ans
