from heapq import heappop, heappush, heapify


class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        (i, j) = (0, 0)
        ans = 0
        length = len(piles)
        while i + j < length - 1:
            i += 1
            j += 2
            ans += piles[-j]
        return ans
