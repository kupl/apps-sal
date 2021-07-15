class Solution:
     def isSubsequence(self, s, t):
         """
         :type s: str
         :type t: str
         :rtype: bool
         """
         t= iter(t)
         return all(i in t for i in s)
