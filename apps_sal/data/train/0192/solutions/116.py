class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        triples = []

        count = len(piles)
        while count > 0:
            newTrip = []
            newTrip = [piles[0], piles[-2], piles[-1]]
            triples.append(newTrip)
            piles.pop(0)
            piles.pop(-2)
            piles.pop(-1)
            count = len(piles)

        maxCoins = 0
        for i in range(len(triples)):
            maxCoins += triples[i][1]
        return maxCoins
