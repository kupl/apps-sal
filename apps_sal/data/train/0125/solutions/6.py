class Solution:
     def superPow(self, a, b):
         """
         :type a: int
         :type b: List[int]
         :rtype: int
         """
         def eular(mod):
             res, a = mod, mod
             i = 2
             while i * i <= a:
                 if a % i == 0:
                     res = res // i * (i - 1)
                     while a % i == 0:
                         a //= i
                 i += 1
             if a > 1:
                 res = res // a * (a - 1)
             return res
         def qpow(x, n, mod):
             res = 1
             while n > 0:
                 if n&1 != 0:
                     res = res * x % mod
                 x = x * x % mod
                 n >>= 1
             return res
         
         phi = eular(1337)
         n = 0
         for num in b:
             n = (n*10 % phi + num) % phi
         return qpow(a, n, 1337)
