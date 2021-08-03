class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort(reverse=True)
        ans = 0
        i = 1

        while i < n:
            ans += piles[i]
            i += 2
            n -= 1

        return ans
