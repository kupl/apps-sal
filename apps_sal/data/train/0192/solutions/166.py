class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        return self.helper(piles)

    def helper(self, piles):
        if not piles:
            return 0

        mx = piles[-1]
        mx2 = piles[-2]
        mn = piles[0]
        piles.pop(0)
        piles.pop()
        piles.pop()
        return mx2 + self.helper(piles)
