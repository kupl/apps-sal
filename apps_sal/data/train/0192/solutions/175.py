class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        a = 0
        first, moke, myself = 0, 0, 0
        i = 0
        j = len(piles) - 1
        while(i < j):
            first += piles[j]
            j -= 1
            myself += piles[j]
            j -= 1
            moke += piles[i]
            i += 1

        return myself
