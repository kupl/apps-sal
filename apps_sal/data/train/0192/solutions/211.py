class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans = 0
        piles.sort()
        i = len(piles) - 2
        j = 0
        while(i >= j):
            ans = ans + piles[i]
            i = i - 2
            j = j + 1
        return ans
