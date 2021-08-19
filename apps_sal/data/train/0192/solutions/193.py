class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        res = 0
        print(piles)
        for i in range(1, len(piles) - len(piles) // 3, 2):
            print(piles[i])
            res += piles[i]
        return res
