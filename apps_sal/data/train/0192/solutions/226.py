class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)/3
        piles.sort()
        res = []
        for i in range(2, 2*int(n)+1, 2):
            res.append(piles[-i])
        return sum(res)
