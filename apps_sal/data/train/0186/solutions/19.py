class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # since cost limit is 5000, we can add 5000
        # to dp size to avoid checking c < target
        dp = [0] + [-1] * (target + 5000)
        for t in range(1, target + 1):
            for i, c in enumerate(cost):
                # the new digit is i + 1, the previous digit dp[t - 1] move 1 step to left
                dp[t] = max(dp[t], dp[t - c] * 10 + (i + 1))
        # since we set dp initial value to be -1, question require 0 if not found.
        return str(max(dp[target], 0))
