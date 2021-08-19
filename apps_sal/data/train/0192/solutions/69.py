from collections import deque


class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        coins = deque(sorted(piles, reverse=True))
        share = 0
        while coins:
            coins.pop()
            coins.popleft()
            share += coins.popleft()
        return share
