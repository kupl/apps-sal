class Solution:
    def coinChange(self, nums: List[int], amount: int) -> int:
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in nums]) + 1

        return [dp[amount], -1][dp[amount] == MAX]

