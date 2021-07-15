class Solution:
     def findLUSlength(self, strs):
         """
         :type strs: List[str]
         :rtype: int
         """
         def check(a,b):
             i=0
             for ai in a:
                 while i<len(b) and ai!=b[i]:
                     i+=1
                 if i==len(b):
                     return False
                 else:
                     i+=1
             return True
         ans=-1
         for i,a in enumerate(strs):
             for j,b in enumerate(strs):
                 if i!=j and check(a,b):
                     break
             else:
                 ans=max(ans,len(a))
         return ans
