class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        while piles:
            big = piles.pop()
            ans += piles.pop()
            smol = piles.pop(0)
        return ans
