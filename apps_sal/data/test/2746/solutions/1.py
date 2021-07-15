class Solution:
     def compareVersion(self, version1, version2):
         v1, v2 = [int(i) for i in version1.split('.')], [int(i) for i in version2.split('.')]
         if len(v1) > len(v2): v2 += [0] * (len(v1) - len(v2))
         if len(v1) < len(v2): v1 += [0] * (len(v2) - len(v1))   
         for i in range(len(v1)):
             if v1[i] > v2[i]: return 1
             if v1[i] < v2[i]: return -1
         return 0

