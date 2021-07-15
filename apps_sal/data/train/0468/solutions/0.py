class Solution:
     def fractionToDecimal(self, numerator, denominator):
         """
         :type numerator: int
         :type denominator: int
         :rtype: str
         """
         if numerator*denominator < 0:
             add_negative = True
         else:
             add_negative = False
         numerator, denominator = abs(numerator), abs(denominator)
         
         integer_part = int(numerator//denominator)
         new_numerator = numerator-integer_part*denominator
         dict_residuals = {}
         digit_location = 0
         digit_array = []
         residual = new_numerator
         if residual == 0:
             if add_negative:
                 return "-"+str(integer_part)
             else:
                 return str(integer_part)
         is_repeating = True
         dict_residuals[residual] = 0
         while True:
             new_digit, residual = self.single_digit(residual, denominator)
             digit_location += 1
             if residual == 0:
                 dict_residuals[residual] = digit_location
                 digit_array.append(str(new_digit))
                 is_repeating = False
                 break
             elif residual in dict_residuals.keys():
                 digit_array.append(str(new_digit))
                 is_repeating = True
                 break
             else:
                 dict_residuals[residual] = digit_location
                 digit_array.append(str(new_digit))
 
         if not is_repeating:
             result = str(integer_part)+"."+"".join(digit_array)
         else:
             loc = dict_residuals[residual]
             result = str(integer_part)+"."+"".join(digit_array[0:loc])+"("+"".join(digit_array[loc:])+")"
         if add_negative:
             return "-"+result
         else:
             return result
     
     def single_digit(self, value, denominator):
         return int((10*value)//denominator), (10*value)%denominator
