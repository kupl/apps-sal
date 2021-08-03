class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        # solution 1: use sort
        # Time-O(nlogn) Space-O(n)
        piles.sort(reverse=True)
        return sum(piles[1:len(piles) // 3 * 2:2])
