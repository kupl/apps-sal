class Solution:
     def findLUSlength(self, strs):
         """
         :type strs: List[str]
         :rtype: int
         """
         answer = -1
         for i in range(len(strs)):
             x = strs[i]
             if len(x) > answer and all([not self.isSubsequence(x, strs[j]) for j in range(len(strs)) if i != j]):
                 answer = len(x)
         return answer
 
     def isSubsequence(self, sub, sup):
         i = j = 0
         while i < len(sub) and j < len(sup):
             if sub[i] == sup[j]:
                 i += 1
             j += 1
         return i == len(sub)
