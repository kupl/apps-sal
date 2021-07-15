class Solution:
     def hIndex(self, citations):
         """
         :type citations: List[int]
         :rtype: int
         """
         if len(citations) == 0:
             return 0
         
         maxCita = -sys.maxsize - 1
         for citation in citations:
             maxCita = max(maxCita, citation)
             
         start = 0
         end = maxCita
         
         while start + 1 < end:
             mid = start + (end - start) // 2
             if self.countAtleast(mid, citations) == mid:
                 return mid
             elif self.countAtleast(mid, citations) > mid:
                 start = mid
             else:
                 end = mid
                 
         if self.countAtleast(end, citations) >= end:
             return end
         else:
             return start
         
     def countAtleast(self, cita, citations):
         count = 0
         for citation in citations:
             if citation >= cita:
                 count += 1
         return count
