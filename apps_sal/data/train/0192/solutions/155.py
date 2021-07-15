class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        count = 0
        while len(piles) >0:
            piles.pop(len(piles)-1)
            piles.pop(0)
            count = count + piles.pop(len(piles)-1)
        return count

