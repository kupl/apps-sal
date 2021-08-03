class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans = 0
        piles.sort()
        while len(piles) > 0:
            alice = piles[len(piles) - 1]
            piles.pop()
            ans += piles[len(piles) - 1]
            piles.pop()
            bob = piles[0]
            piles.pop(0)
        return ans
