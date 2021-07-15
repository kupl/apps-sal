class Solution:
     def isSubsequence(self, s, t):
         """
         :type s: str
         :type t: str
         :rtype: bool
         """
         start = 0
         for i in range(len(s)):
             index = t[start:].find(s[i])
             print(index)
             if index == -1:
                 return False
             else:
                 index += start
                 start = index+1
         return True

