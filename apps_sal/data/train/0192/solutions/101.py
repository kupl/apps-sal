class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles.reverse()
        count = 0

        i = 0
        numTimes = 0
        while numTimes < len(piles) // 3:
            count += piles[i + 1]
            i += 2
            numTimes += 1
        return count
