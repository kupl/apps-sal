class Solution:
    from collections import deque

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles) // 3
        s = piles[n:n * 3]
        return sum([s[i] for i in range(len(s)) if i % 2 == 0])
