class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles) // 3
        num = 0
        for i in range(n):
            num += piles[i * 2 + 1]
        return num
