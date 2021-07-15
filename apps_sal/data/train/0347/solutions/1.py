class Solution:
     def checkInclusion(self, s1, s2):
         """
         :type s1: str
         :type s2: str
         :rtype: bool
         """
         l1, l2 = len(s1), len(s2)
         c1 = [0] * 128
         n = 0
         for i in s1:
             c = ord(i)
             if c1[c] == 0: n += 1
             c1[c] += 1
         for i in range(l2):
             j = i - l1
             if j >= 0:
                 c = ord(s2[j])
                 if not c1[c]: n += 1
                 c1[c] += 1
             c = ord(s2[i])
             c1[c] -= 1
             if not c1[c]:
                 n -= 1
                 if not n: return True
         return False
