class Solution:
     def superPow(self, a, b):
         """
         :type a: int
         :type b: List[int]
         :rtype: int
         """
         # return pow(a, int(''.join(map(str, b))), 1337)
         from functools import reduce
         k=reduce(lambda x,y:x*10+y, b)
         # print(k)
         # return pow(a,k)%1337
         return pow(a, k, 1337)
