from heapq import heappush, heappop
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = {}
        for i in arr:
            d[i] = d.get(i,0)+1
          
        heap = []
        for i in d.keys():
            heappush(heap, (d[i]))
            
        while k >0:
            count = heappop(heap)
            k-= count
            if k < 0:
                return len(heap) + 1
            
        return len(heap)
