class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles)[-2:-2*(len(sorted(piles))//3)-1:-2])
