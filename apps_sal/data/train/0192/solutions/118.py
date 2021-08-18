class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        wallet = 0
        while piles:
            piles.pop()
            wallet += piles.pop()
            del piles[0]
        return wallet
