class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        wallet = 0
        start = 0
        end = len(piles) - 1
        while start <= end:
            start += 1
            end -= 1
            wallet += piles[end]
            end -= 1
        return wallet
