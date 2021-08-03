class Solution:
    def maxCoins(self, p: List[int]) -> int:
        p.sort()
        max_coins = 0
        i = len(p) // 3
        while i < len(p):
            max_coins += p[i]
            i += 2
        return max_coins
