class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        result = 0
        piles.sort(reverse=True)
        i = 0
        j = len(piles) - 1
        while i < j - 1:
            result += piles[i + 1]
            i += 2
            j -= 1
        return result
