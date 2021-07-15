import heapq

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        max_coins_for_me = 0
        sorted_piles = sorted(piles)
        top = len(piles) - 1
        for i in range(len(piles) // 3):
            max_coins_for_me += sorted_piles[top-1]
            top = top - 2
        return max_coins_for_me
