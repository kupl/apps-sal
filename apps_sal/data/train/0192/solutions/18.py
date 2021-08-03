import heapq


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        choice = heapq.nlargest(len(piles) // 3 * 2, piles)
        ans = 0
        for i in range(1, len(choice), 2):
            ans += choice[i]
        return ans
