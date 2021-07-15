class Solution:        
     def fractionToDecimal(self, numerator, denominator):
         sign = '' if not numerator or (numerator < 0) is (denominator < 0) else '-'
         numerator, denominator = abs(numerator), abs(denominator)
         p, q = divmod(abs(numerator), abs(denominator))
         res, decimal, mod, count = str(p), [], {q: 0}, 0
         while q:
             p, q = divmod(q * 10, denominator)
             decimal.append(str(p))
             if q in mod:
                 idx = mod[q]
                 decimal.insert(idx, '('), decimal.append(')')
                 break
             count += 1
             mod[q] = count
         return sign + res + '.' + ''.join(decimal) if decimal else sign + res
