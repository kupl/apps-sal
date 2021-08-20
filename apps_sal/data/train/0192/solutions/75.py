from collections import deque


class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        l = len(piles)
        n = l // 3
        piles.sort()
        piles = deque(piles)
        ans = 0
        while piles:
            piles.pop()
            ans += piles.pop()
            piles.popleft()
        return ans
