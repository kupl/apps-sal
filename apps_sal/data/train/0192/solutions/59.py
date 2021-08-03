class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        ans = 0
        for i in range(int(len(piles) / 3)):
            ans = ans + piles[2 * i + 1]
        return ans
