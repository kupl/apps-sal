class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        dp = [[-1 for i in range(len(piles))] for j in range(len(piles))]
        left = 0
        right = len(piles) - 1
        out = self.helper(piles, left, right, dp, 0)
        if out > sum(piles) - out:
            return True
        return False

    def helper(self, piles, left, right, dp, flag):
        if left > right:
            return 0
        if dp[left][right] != -1:
            return dp[left][right]
        if flag == 0:
            one = self.helper(piles, left + 1, right, dp, 1) + piles[left]
            two = self.helper(piles, left, right - 1, dp, 1) + piles[right]
            dp[left][right] = max(one, two)
            return max(one, two)
        else:
            one = self.helper(piles, left + 1, right, dp, 0)
            two = self.helper(piles, left, right - 1, dp, 0)
            dp[left][right] = min(one, two)
            return min(one, two)
