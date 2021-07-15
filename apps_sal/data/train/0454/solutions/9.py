class Solution:
     def swap(self, i, c):
         for ii in range(len(self.res))[::-1]:
             if self.res[ii] == c:
                 a, b = self.res[i], self.res[ii]
                 self.res = self.res[:i] + b + self.res[i + 1:]
                 self.res = self.res[:ii] + a + self.res[ii + 1:]
                 break
                     
     def maximumSwap(self, num):
         """
         :type num: int
         :rtype: int
         """
         s = str(num)
         l = sorted(list(s), reverse=True)
         self.res = s
 
         for i, char in enumerate(s):
             if char != l[i]:
                 self.swap(i, l[i])
                 break
 
         return int(self.res)
