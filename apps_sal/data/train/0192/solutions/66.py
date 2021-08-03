class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        mine = 0
        s = list(sorted(piles, reverse=True))
        for i in range(len(s) // 3):
            mine += s[2 * i + 1]
        return mine
