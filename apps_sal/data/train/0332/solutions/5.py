class Solution:
     def countSubstrings(self, s):
         """
         :type s: str
         :rtype: int
         """
         
         # manacher, find Z
         s = '^#' + '#'.join(s) + '#$'
         Z = [1] * len(s)
         center, right = 0, 0
         for i in range(len(s)-1): # 注意 i不能取到 $
             if i < right:
                 i_mirror = 2 * center - i
                 Z[i] = min(Z[i_mirror], right - i + 1)
             while s[i+Z[i]] == s[i-Z[i]]:
                 Z[i] += 1
             if i + Z[i] - 1 > right:
                 center, right = i, i + Z[i] - 1
         
         # sum Z
         return sum(z//2 for z in Z)
