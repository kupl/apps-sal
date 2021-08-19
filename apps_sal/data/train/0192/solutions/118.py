class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        wallet = 0
        while piles:
            # Alices pile
            piles.pop()
            # My pile
            wallet += piles.pop()
            # Bob pile
            del piles[0]
        return wallet
