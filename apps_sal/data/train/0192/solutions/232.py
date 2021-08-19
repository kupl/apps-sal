class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        count = 0
        piles.sort()
        l = len(piles)
        n = l // 3
        j = l - 2
        k = 0
        while k < n:
            count = count + piles[j]
            j = j - 2
            k = k + 1
        return count
