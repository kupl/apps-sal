class Solution:
     def isScramble(self, s1, s2):
         if sorted(s1) != sorted(s2): return False
         if len(s1) < 4 or s1 == s2: return True
         f = self.isScramble
         for i in range(1, len(s1)):
             if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or f(s1[:i], s2[-i:]) and f(s1[i:], s2[:len(s1) - i]):
                 return True
         return False

