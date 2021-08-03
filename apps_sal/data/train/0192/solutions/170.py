class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        me = 0
        piles.sort()

        while piles:
            arr = []
            arr += piles.pop(),
            arr += piles.pop(),
            arr += piles.pop(0),
            arr.sort()

            me += arr.pop(1)

        return me
