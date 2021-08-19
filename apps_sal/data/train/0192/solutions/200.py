class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        print(piles)
        n = len(piles)
        s = 0
        for i in range(n // 3):
            print(n - 1 - (2 * i + 1))
            s += piles[n - 1 - (2 * i + 1)]
        return s
