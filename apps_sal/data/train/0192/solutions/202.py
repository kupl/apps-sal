class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        heap = [-x for x in piles]
        heapq.heapify(heap)

        rounds = count = 0

        while len(heap) > rounds:
            _ = heapq.heappop(heap)
            count -= heapq.heappop(heap)
            rounds += 1

        return count
