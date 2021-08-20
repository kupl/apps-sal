class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        if not piles:
            return 0
        piles.sort()
        coins = 0
        n = len(piles)
        index = n - 2
        for i in range(n // 3):
            coins += piles[index]
            index -= 2
        return coins
