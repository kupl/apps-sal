class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) / 3
        res = 0
        p = sorted(piles)
        for i in range(int(n)):
            p.pop(-1)
            p.pop(0)
            res += p[-1]
            p.pop(-1)
        return res
