class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i = 0
        j = len(piles) - 1
        ans = 0
        while i < j:
            j -= 1
            ans += piles[j]
            j -= 1
            i += 1
        return ans
