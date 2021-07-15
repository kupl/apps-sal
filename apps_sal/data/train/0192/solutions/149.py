class Solution:
    # O(nlgn) solution with O(1) space complexity
    def maxCoins(self, piles: List[int]) -> int:
        # First sort
        piles.sort()
        res = 0
        while piles:
            first = piles.pop(-1)
            second = piles.pop(-1)
            third = piles.pop(0)
            res += second
        return res
