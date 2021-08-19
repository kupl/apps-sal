class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        numOfTurns = int(len(piles) / 3)
        meAndAlice = piles[numOfTurns:]
        myTotal = 0
        for i in range(0, len(meAndAlice), 2):
            myTotal += meAndAlice[i]
        return myTotal
