class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles)
        ret = 0
        for i in range(int(n / 3)):
            ret += piles[2 * i + 1]
        return ret
