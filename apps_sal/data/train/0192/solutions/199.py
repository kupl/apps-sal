class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans = 0
        piles.sort()
        n = len(piles)
        for i in range(n - 2, n // 3 - 1, -2):
            ans += piles[i]

        return ans
