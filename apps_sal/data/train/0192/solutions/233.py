from collections import deque


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles = deque(piles)
        total = 0
        ptr1, ptr2 = len(piles) - 2, 0
        while ptr2 < ptr1:
            total += piles[ptr1]
            ptr1 -= 2
            ptr2 += 1
        return total
