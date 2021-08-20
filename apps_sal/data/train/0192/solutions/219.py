class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        res = 0
        (alice, me, bob) = (0, 1, -1)
        while me < len(piles) + bob:
            res += piles[me]
            alice += 2
            me += 2
            bob -= 1
        return res
