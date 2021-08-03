class Solution:
    from collections import deque

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles) // 3
        s = 0
        for i in range(n, n * 3, 2):
            s += piles[i]
        return s
