class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        while len(piles) != 0:
            piles.pop(0)
            piles.pop(-1)
            ans += piles.pop(-1)
        return ans
