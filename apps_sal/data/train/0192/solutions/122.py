class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        if not piles:
            return 0

        rounds = len(piles) // 3

        max_heap = []
        min_heap = []

        for n in piles:
            heapq.heappush(max_heap, -n)
            heapq.heappush(min_heap, n)
        res = 0

        while rounds > 0:
            rounds -= 1

            alex, me = -heapq.heappop(max_heap), -heapq.heappop(max_heap)
            # bob = heapq.heappop(min_heap)

            res += me

        return res
