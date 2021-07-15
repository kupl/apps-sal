class Solution:
     def hIndex(self, citations):
         """
         :type citations: List[int]
         :rtype: int
         """
         citations.sort(reverse=True)
         for idx in range(len(citations)):
             if idx + 1> citations[idx]:
                 return idx
         return len(citations)

