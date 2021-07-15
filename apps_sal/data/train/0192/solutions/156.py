class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ret = 0
        while piles:
            piles.pop()
            ret += piles.pop()
            piles.pop(0)
        
        return ret
