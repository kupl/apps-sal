class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = 1)
        res = 0
        rounds = len(piles)//3
        for r in range(rounds):
            res += piles[r*2 + 1]
        return res
