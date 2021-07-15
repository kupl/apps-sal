class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        length = len(piles)
        sorted_piles = sorted(piles, reverse = True)
        if length == 3:
            return sorted_piles[1]
        n = length / 3
        count, res = 0, 0
        for i in range(1, length, 2):
            if count == n:
                return res
            res += sorted_piles[i]
            count += 1
