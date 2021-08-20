class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        sorted_piles = list(sorted(piles))
        s = 0
        while len(sorted_piles) > 3:
            triplet = [sorted_piles.pop(0)] + [sorted_piles.pop(-2)] + [sorted_piles.pop(-1)]
            s += triplet[1]
        triplet = [sorted_piles.pop(0)] + [sorted_piles.pop(-2)] + [sorted_piles.pop(-1)]
        s += triplet[1]
        return s
