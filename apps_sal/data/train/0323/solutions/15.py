class Solution:
     def isInterleave(self, s1, s2, s3):
         """
         :type s1: str
         :type s2: str
         :type s3: str
         :rtype: bool
         """
         if len(s1) + len(s2) != len(s3):
             return False
         
         res = [[False for j in range(1+len(s2))] for i in range(1+len(s1))]
         for i in range(1+len(s1)):
             for j in range(1+len(s2)):
                 if i == 0 and j == 0:
                     res[i][j] = True
                 elif i == 0:
                     res[i][j] = res[i][j-1] and s3[i+j-1] == s2[j-1]
                 elif j == 0:
                     res[i][j] = res[i-1][j] and s3[i+j-1] == s1[i-1]
                 else:
                     res[i][j] = res[i][j] or (s3[i+j-1] == s1[i-1] and res[i-1][j])
                     res[i][j] = res[i][j] or (s3[i+j-1] == s2[j-1] and res[i][j-1])
         return res[len(s1)][len(s2)]

