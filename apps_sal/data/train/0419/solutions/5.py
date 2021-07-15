class Solution:
     def bulbSwitch(self, n):
         """
         :type n: int
         :rtype: int
         """
         # if n == 0: return 0
         # if n <= 2: return 1
         # cur = 1
         # for i in range(2, int(math.sqrt(n))+1):
         #     a = int(math.sqrt(i))
         #     if a*a == i: cur += 1
         return int(math.sqrt(n))

