class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        ans = 0
        i = 0
        j = len(piles) - 1

        while(i < j):
            ans += piles[j - 1]
            j -= 2
            i += 1
        return ans
