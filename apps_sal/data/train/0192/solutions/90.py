import heapq


class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        maxheap = []
        for i in range(len(piles)):
            heapq.heappush(maxheap, piles[i] * -1)
        mine = 0
        size = len(maxheap)
        while size > 0:
            heapq.heappop(maxheap)
            middle = heapq.heappop(maxheap)
            middle *= -1
            mine += middle
            size -= 3
        return mine
