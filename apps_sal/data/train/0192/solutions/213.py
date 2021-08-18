class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles, reverse=True)
        ans = []
        for i in range(0, len(piles) // 3 * 2, 2):
            ans.append(piles[i + 1])
        return sum(ans)
