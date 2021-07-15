class Solution:
     def isInterleave(self, s1, s2, s3):
         """
         :type s1: str
         :type s2: str
         :type s3: str
         :rtype: bool
         """
         if not s1:
             if s2 != s3:
                 return False
             else:
                 return True
         if not s2:
             if s1 != s3:
                 return False
             else:
                 return True
         if len(s1) + len(s2) != len(s3):
             return False
         f = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
         f[0][0] = True
         for i in range(1, len(s1) + 1):
             if s1[i - 1] == s3[i - 1] and f[i - 1][0]:
                 f[i][0] = True
         for j in range(1, len(s2) + 1):
             if s2[j - 1] == s3[j - 1] and f[0][j - 1]:
                 f[0][j] = True
         for i in range(1, len(s1) + 1):
             for j in range(1, len(s2) + 1):
                 f[i][j] = (f[i - 1][j] and (s3[i + j - 1] == s1[i - 1])) or ((s3[i + j - 1] == s2[j - 1]) and f[i][j - 1])
         return f[-1][-1]
