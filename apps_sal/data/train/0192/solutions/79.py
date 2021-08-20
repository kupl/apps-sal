class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        (i, j) = (0, len(piles) - 2)
        ans = 0
        while i < j:
            ans += piles[j]
            j -= 2
            i += 1
        return ans
