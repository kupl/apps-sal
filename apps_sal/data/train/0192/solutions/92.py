class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        i = 0
        j = len(piles) - 1
        ans = 0
        while i < j:
            ans += piles[j - 1]
            i += 1
            j -= 2
        return ans
