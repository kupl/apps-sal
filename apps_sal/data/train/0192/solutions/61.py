class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        me, alice, bob = 0, 0, 0
        i = 0
        j = len(piles) - 1
        while i < j - 1:
            bob += piles[i]
            i += 1
            me += piles[j - 1]
            alice += piles[j]
            j -= 2
        return me
