class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        while len(piles) != 0:
            can = []
            can.append(piles.pop())
            can.append(piles.pop())
            can.append(piles.pop(0))
            res += can[1]
            can = []
        return res
