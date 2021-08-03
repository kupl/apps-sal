class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort()
        rounds = int(len(piles) / 3)
        max_el = 0
        while rounds != 0:
            piles.pop()
            max_el += piles[-1]
            piles.pop()
            piles.pop(0)
            rounds -= 1
        return max_el
