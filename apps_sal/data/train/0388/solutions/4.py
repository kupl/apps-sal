class Solution:
     def hIndex(self, citations):
         """
         :type citations: List[int]
         :rtype: int
         """
         length = len(citations)
         if (length == 0):
             return 0
         
         citations.sort()
         
         for idx, citation in enumerate(citations):
             counts_bigger_equal_curr_citation = length - idx
             if citation >= counts_bigger_equal_curr_citation:
                 return counts_bigger_equal_curr_citation
             
         return 0

