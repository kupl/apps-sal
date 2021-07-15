class Solution:
     def fractionToDecimal(self, numerator, denominator):
         """
         :type numerator: int
         :type denominator: int
         :rtype: str
         """
         negative = (numerator < 0) != (denominator < 0)
         
         numerator = abs(numerator)
         denominator = abs(denominator)
         
         pre_decimal = numerator // denominator
         remainder = numerator % denominator
         
         hash_map = {}
         hash_map[remainder] = 0
         post_decimal = []
         def build_fraction(numerator, denominator, post_decimal, depth):
             val = numerator // denominator
             post_decimal.append(val)
             remainder = numerator % denominator
             if remainder in hash_map:
                 out = [str(i) for i in post_decimal[:hash_map[remainder]]]
                 rep = "("
                 rep += "".join([str(i) for i in post_decimal[hash_map[remainder]:depth]])
                 rep += ")"
                 rep = "" if rep == "(0)" else rep
                 out = "".join(out)
                 return out+rep
             else:
                 hash_map[remainder] = depth
             return build_fraction(10*remainder, denominator, post_decimal, depth+1)
             
         suffix = build_fraction(10*remainder, denominator, post_decimal, 1)
         
         out = str(pre_decimal) + "." + suffix
         if out[-1] == ".":
             out = out[:-1]
         out = out if not negative else "-"+out
         return out if out != "-0" else "0"
         

