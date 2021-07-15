class Solution:
     def findLUSlength(self, strs):
         """
         :type strs: List[str]
         :rtype: int
         """
         def issub(w1, w2):
             i = 0
             for w in w2:
                 if i < len(w1) and w1[i] == w:
                     i += 1
             return i == len(w1)
         strs.sort(key = len, reverse = True)
         for s in strs:
             strs_copy = strs.copy()
             strs_copy.remove(s)
             if all(not issub(s, ss) for ss in strs_copy):
                 return len(s)
         return -1

