class Solution:
     def removeDuplicateLetters(self, s):
         """
         :type s: str
         :rtype: str
         """
         
         if len(s) <= 1:
             return s
         
         
         for c in sorted(list(set(s))):
             suffix = s[s.index(c):]
             if set(s) == set(suffix):
                 return c + self.removeDuplicateLetters(suffix.replace(c, ''))
         
         return ''
                     
         
         
             

