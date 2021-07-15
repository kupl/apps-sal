class Solution:
     def isMatch(self, s, p):
         """
         :type s: str
         :type p: str
         :rtype: bool
         """
         '''维护两个下标，逐个比较，如果pj为*，则记录*的位置，将*后一个元素与si进行比较，如果不相等，则将i从记录的位置+1，重新比较'''
         i=0
         j=0
         star=-1
         lenp=len(p)
         while i<len(s):
             if j<lenp and (s[i]==p[j] or p[j]=='?'):
                 i+=1
                 j+=1
             elif j<lenp and p[j]=='*':
                 star=j
                 mi=i
                 j+=1
             elif star!=-1:
                 mi+=1
                 i=mi
                 j=star+1
             else:
                 return False
         while j<lenp and p[j]=='*':
             j+=1
         
         return j==lenp
