class Solution:
     def isSubsequence(self, s, t):
         """
         :type s: str
         :type t: str
         :rtype: bool
         """
         i = 0
         if not s:
             return True
         m, n = len(t), len(s)
         for ch in t:
             if ch == s[i]:
                 if i == n-1:
                     return True
                 i += 1
         return False
