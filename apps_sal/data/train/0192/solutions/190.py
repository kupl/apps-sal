class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(key=lambda x: -x)
        return sum(piles[1:len(piles) // 3 * 2:2])
