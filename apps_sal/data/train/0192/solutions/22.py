class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        num = int(len(piles) / 3)
        sor = sorted(piles)
        count = 0
        for i in range(1, num + 1):
            count += sor[num * 3 - i * 2]
        return count
