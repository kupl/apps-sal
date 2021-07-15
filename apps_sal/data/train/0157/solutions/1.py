class Solution:
     def isMatch(self, s, p):
         """
         :type s: str
         :type p: str
         :rtype: bool
         """
         m = len(s)
         n = len(p)
         starj = -1
         last_match = -1
         i = j = 0
         while i<m:
             if j<n and (s[i]==p[j] or p[j]=='?'):
                 i+=1
                 j+=1
             elif j<n and p[j]=='*':
                 starj = j
                 j += 1
                 last_match = i
             elif starj!=-1:
                 j = starj+1
                 last_match +=1
                 i = last_match
             else:
                 return False
         
         while j<n and p[j]=='*':
             j+=1
         return j==n
                 

