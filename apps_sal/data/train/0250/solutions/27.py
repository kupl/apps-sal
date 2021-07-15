import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        heap=[]
        rate=sorted(((w/q, q) for w, q in zip(wage, quality)))
        qsum=0
        res=float('inf')
        for r, q in rate:
            heapq.heappush(heap, -q)
            qsum+=q
            if len(heap)>K:
                qsum+=heapq.heappop(heap)
            if len(heap)==K:
                res=min(res, r*qsum)
        return res
