import heapq


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res = 0
        heap = []
        for p in piles:
            heapq.heappush(heap, -p)
                
        for i in range(len(piles) // 3):
            heapq.heappop(heap)
            res += -heapq.heappop(heap)
        
        return res
