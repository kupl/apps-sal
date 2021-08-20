from collections import deque


class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles = deque(sorted(piles))
        my_coins = 0
        while piles:
            piles.pop()
            piles.popleft()
            my_coins += piles.pop()
        return my_coins
