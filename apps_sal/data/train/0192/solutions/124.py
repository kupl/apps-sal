class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        numCoins = 0
        piles.sort()

        while len(piles) > 0:
            # give alice
            piles.pop()
            # give me
            numCoins += piles.pop()
            # give bob
            piles.pop(0)

        return numCoins
