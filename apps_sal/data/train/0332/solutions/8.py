class Solution:
     def countSubstrings(self, s):
         """
         :type s: str
         :rtype: int
         """
         s=','+s+'.'
         ans=0
         for i in range(1,len(s)-1):
             j=1
             while s[i+j]==s[i-j]:
                 j+=1
             ans+=j
         for i in range(1,len(s)-1):
             j=0
             while s[i-j]==s[i+1+j]:
                 j+=1
             ans+=j
         return ans
