class Solution:
     def fractionToDecimal(self, numerator, denominator):
         """
         :type numerator: int
         :type denominator: int
         :rtype: str
         """
         prev = []
         prevdigits = []
         s = ""
         if denominator < 0:
            numerator *=-1
            denominator *=-1
         if numerator < 0:
            numerator *= -1
            s += "-"
         d, numerator = divmod(numerator,denominator) 
         s += str(d)
         if numerator == 0:
            return s
         s += "."
         while numerator not in prev and numerator != 0:
            prev.append(numerator)
            numerator *= 10
            d, numerator = divmod(numerator,denominator) 
            prevdigits.append(str(d))
            numerator %= denominator
         if numerator == 0:
            return s+"".join(prevdigits)
         #print(prev, prevdigits)
         i  = prev.index(numerator)
         return s+"".join(prevdigits[0:i])+"("+"".join(prevdigits[i:])+")"

