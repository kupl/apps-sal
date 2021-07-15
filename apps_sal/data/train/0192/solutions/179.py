class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        wallet = 0
        start = 0
        end = len(piles) - 1
        while start <= end:
            # Bob pile
            start += 1
            # Alices pile
            end -= 1
            # My pile
            wallet += piles[end]
            end -= 1
        return wallet

