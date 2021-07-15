class Solution:
     def superPow(self, a, b):
         """
         :type a: int
         :type b: List[int]
         :rtype: int
         a %= 1337
         if len(b) == 1:
             return self.powMod(a, b[0])
         return self.powMod(self.superPow(a, b[:-1]), 10) * self.powMod(a, b[-1]) % 1337
         """
         res = 1
         x = a % 1337
         for y in b[::-1]:
             res = (res * (x ** y)) % 1337
             x = (x ** 10) % 1337
         return res

