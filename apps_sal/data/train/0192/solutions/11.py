class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(key=lambda k: k * -1)
        return sum(piles[1:len(piles) // 3 * 2:2])

        # 9, 8, 1
        # 7, 6, 2
        # 5, 4, 3
