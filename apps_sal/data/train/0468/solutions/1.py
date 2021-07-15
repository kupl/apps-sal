class Solution:
     def fractionToDecimal(self, numerator, denominator):
         """
         :type numerator: int
         :type denominator: int
         :rtype: str
         """    
         res = ""
         if numerator * denominator < 0:
             res += '-'
         if numerator % denominator == 0:
             return str(numerator // denominator)
         numerator = abs(numerator)
         denominator = abs(denominator)
         res += str(numerator // denominator)
         res += '.'
         numerator %= denominator
         i = len(res)
         table = collections.defaultdict(int)
         while numerator != 0:
             if numerator not in table:
                 table[numerator] = i
             else:
                 i = table[numerator]
                 res = res[:i] + '(' + res[i:] + ')'
                 return res
             numerator *= 10
             res += str(numerator // denominator)
             numerator %= denominator
             i += 1
         return res
