class Solution:
     def hIndex(self, citations):
         """
         :type citations: List[int]
         :rtype: int
         """
 #         if len(citations) == 0:
 #             return 0
         
 #         maxCita = -sys.maxsize - 1
 #         for citation in citations:
 #             maxCita = max(maxCita, citation)
             
 #         start = 0
 #         end = maxCita
         
 #         while start + 1 < end:
 #             mid = start + (end - start) // 2
 #             if self.countGreater(mid, citations) > mid:
 #                 start = mid
 #             else:
 #                 end = mid
                 
 #         if self.countGreater(end, citations) <= end:
 #             return end
 #         else:
 #             return start
         
 #     def countGreater(self, cita, citations):
 #         count = 0
 #         for citation in citations:
 #             if citation > cita:
 #                 count += 1
 #         return count
     
     
         if len(citations) == 0:
             return 0
         h = [0 for i in range(len(citations) + 1)]
         for citation in citations:
             if citation >= len(citations):
                 h[len(citations)] += 1
             else:
                 h[citation] += 1
         
         i = len(citations) - 1
         while i >= 0:
             h[i] += h[i + 1]
             if h[i + 1] >= i + 1:
                 return i + 1
             i -= 1
         return 0
             

