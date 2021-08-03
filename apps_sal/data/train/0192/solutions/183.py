class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        my_coins = 0

        piles.sort()
        count = len(piles) / 3
        i = 0
        j = -2
        k = -1
        while count > 0:
            my_coins += piles[j]
            i += 1
            j -= 2
            k -= 2
            count -= 1

        return my_coins
