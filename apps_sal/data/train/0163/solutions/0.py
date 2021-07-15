class Solution:
     def isSubsequence(self, s, t):
         """
         :type s: str
         :type t: str
         :rtype: bool
         """
         if len(s) > len(t):
             return False
         for i in s:
             if i in t:
                 index = t.find(i)
                 t = t[index + 1:]
             else:
                 return False
         return True
