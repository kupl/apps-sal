class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l_i, r_i = 0, len(piles)-1
        max_coin = 0
        while l_i < r_i:
            max_coin += piles[r_i-1]
            l_i += 1
            r_i -= 2
        return max_coin

