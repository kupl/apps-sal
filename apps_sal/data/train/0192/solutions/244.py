class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans = 0
        piles.sort(reverse=True)
        for i in range(len(piles) // 3):
            ans += piles[i * 2 + 1]
        return ans
