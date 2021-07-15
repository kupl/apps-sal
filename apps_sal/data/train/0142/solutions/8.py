class Solution:
     def findLUSlength(self, strs):
         """
         :type strs: List[str]
         :rtype: int
         """
         def is_subsequence(s, substr):
             i = 0
             j = 0
             while i < len(s) and j < len(substr):
                 if s[i] == substr[j]:
                     i += 1
                     j += 1
                 else:
                     i += 1
 
             return j == len(substr)
 
         res = -1
         for i in range(len(strs)):
             j = 0
             while j < len(strs):
                 if i == j:
                     j += 1
                     continue
                 if is_subsequence(strs[j], strs[i]):
                     break
                 j += 1  
             if j == len(strs):
                 res = max(res, len(strs[i]))
             
         return res
