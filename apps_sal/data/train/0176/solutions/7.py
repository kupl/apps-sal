class Solution:
     def isScramble(self, s1, s2):
         """
         :type s1: str
         :type s2: str
         :rtype: bool
         """
         if s1 == s2:
             return True
         if len(s1) != len(s2) or sorted(s1) != sorted(s2):
             return False
         dp = self.isScramble
         for i in range(1, len(s1)):
             for j in range(1, len(s2)):
                 if (dp(s1[:i], s2[:j]) and dp(s1[i:], s2[j:])) or (dp(s1[:i], s2[j:]) and dp(s1[i:], s2[:j])):
                     return True
         return False
