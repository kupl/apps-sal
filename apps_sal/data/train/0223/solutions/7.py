class Solution:
     def hIndex(self, citations):
         """
         :type citations: List[int]
         :rtype: int
         """
         citations.sort()
         for i in range(len(citations)-1, -1, -1):
             if citations[i] >= len(citations)-i and (i == 0 or citations[i-1] <= len(citations)-i):
                 return len(citations)-i
         return 0
