class Solution:
     def findContentChildren(self, g, s):
         """
         :type g: List[int]
         :type s: List[int]
         :rtype: int
         """
         g.sort()
         s.sort()
         res = 0 
         Lg,Ls = len(g),len(s)
         i=j=0 
         while i<Lg and j<Ls:
             if s[j] >= g[i]:
                 res += 1
                 j += 1
                 i += 1
             else:
                 j += 1
         return res

