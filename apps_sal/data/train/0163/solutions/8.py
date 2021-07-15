class Solution:
     def isSubsequence(self, s, t):
         if s == "":
             return True
         s_num = 0
         temp = s[s_num]
         for i in t:
             if i == temp:
                 s_num = s_num + 1
                 if s_num >= len(s):
                     return True
                 temp = s[s_num]
         return False

