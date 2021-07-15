class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ret_num = 0
        while piles:
            piles.pop(0)
            piles.pop()
            ret_num += piles.pop()
        return ret_num
