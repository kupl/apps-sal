class Solution:
     def hIndex(self, citations):
         """
         :type citations: List[int]
         :rtype: int
         """
         
         if len(citations) == 0:
             return 0
         else:
             citations.sort()
             i = 0
             while i < len(citations) :
                 if citations[-i-1] >= (i+1):
                     i += 1
                 else:
                     break
             return i

