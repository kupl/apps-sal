class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        size = len(piles)
        time = int(size / 3)
        (i, ans) = (0, 0)
        while i < time:
            ans += piles[size - 2 - i * 2]
            i += 1
        return ans
