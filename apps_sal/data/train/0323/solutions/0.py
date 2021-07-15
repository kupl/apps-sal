class Solution:
     def isInterleave(self, s1, s2, s3):
         """
         :type s1: str
         :type s2: str
         :type s3: str
         :rtype: bool
         """
         if len(s3) != len(s1) + len(s2):
             return False
         if not s1 or not s2:
             return (s1 or s2) == s3
         options = {(0, 0)}
         for char in s3:
             new_options = set()
             for i1, i2 in options:
                 if i1 < len(s1) and char == s1[i1]:
                     new_options.add((i1 + 1, i2))
                 if i2 < len(s2) and char == s2[i2]:
                     new_options.add((i1, i2 + 1))
             options = new_options
             if not options:
                 return False
         return True
