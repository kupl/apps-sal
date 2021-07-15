class Solution:
     def validUtf8(self, data):
         """
         :type data: List[int]
         :rtype: bool
         """
         cont = 0
         for n in data:
             s=format(n, '08b')
             if cont > 0:
                 if s[:2] == '10':
                     cont -= 1
                     continue
                 return False
             if s[0] == '0':
                 continue
             if s[:3] == '110':
                 cont = 1
                 continue
             if s[:4] == '1110':
                 cont = 2
                 continue
             if s[:5] == '11110':
                 cont = 3
                 continue
             return False
         return cont == 0

