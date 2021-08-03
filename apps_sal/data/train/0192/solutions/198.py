class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l = len(piles)
        temp = 2

        sum = 0
        for i in range(l // 3):
            sum = sum + piles[l - temp]
            temp = temp + 2
        return sum
