class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        sort = sorted(piles)
        sort = sort[len(sort) // 3:]
        res = 0
        for i in range(0, len(sort), 2):
            res += sort[i]
        return res
