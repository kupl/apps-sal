class Solution:
     def compareVersion(self, version1, version2):
         """
         :type version1: str
         :type version2: str
         :rtype: int
         """
         
         v1 = version1.split('.')
         v2 = version2.split('.')
         
         len1 = len(v1)
         len2 = len(v2)
         
         for i in range(min(len1, len2)):
             if int(v1[i]) != int(v2[i]):
                 return 1 if int(v1[i]) > int(v2[i]) else -1
             
         (v,t) = (v1,1) if len1 > len2 else (v2,-1)
         for j in v[min(len1,len2):]:
             if int(j) > 0:
                 return t
             
         return 0
         

