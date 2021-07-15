class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        wallet = 0
        while piles:
            piles.pop(-1)
            wallet += piles.pop(-1)
            piles.pop(0)
        return wallet
