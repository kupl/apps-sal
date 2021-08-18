class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res = 0
        piles.sort(reverse=1)
        for i in range(0, (len(piles) // 3) * 2, 2):
            res += piles[i + 1]
            print(res)
        return res
