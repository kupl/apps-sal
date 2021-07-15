class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        length = len(piles)
        maxSum = 0
        for i in range(int(length/3)):
            maxSum += piles[-2]
            piles.pop(-1)
            piles.pop(-1)
            piles.pop(0)
        return maxSum

