class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        numRounds = len(piles) // 3
        ret = 0
        for i in range(len(piles) - 1, numRounds - 1, -2):
            ret += min(piles[i], piles[i - 1])
        return ret
