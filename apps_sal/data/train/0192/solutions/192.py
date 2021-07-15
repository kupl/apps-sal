class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        s_piles = sorted(piles)
        my_coin_ct = 0
        triplet_ct = len(s_piles) // 3
        for i in range(triplet_ct, 0, -1):
            my_coin_ct += s_piles[2 * (i - 1) + triplet_ct]
        return my_coin_ct

