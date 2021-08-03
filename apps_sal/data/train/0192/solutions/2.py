class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        piles.reverse()
        ans = 0
        for i in range(len(piles) // 3):
            ans = ans + piles[2 * i + 1]

        return ans
