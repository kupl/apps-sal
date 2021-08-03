class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        n = len(piles)

        alice_and_me = []
        max_piles = [-p for p in piles]
        heapq.heapify(max_piles)

        out = 0

        seen = 0

        while seen != n // 3:
            alice = heapq.heappop(max_piles)
            out -= heapq.heappop(max_piles)
            seen += 1

        return out
