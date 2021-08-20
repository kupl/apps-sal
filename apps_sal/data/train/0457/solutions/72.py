class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = amount + 1
        coins.sort(reverse=True)
        dp = [MAX] * MAX
        dp[0] = 0
        for i in range(1, MAX):
            dp[i] = min([dp[i - c] if i >= c else MAX for c in coins])
            dp[i] = dp[i] + 1 if dp[i] != MAX else dp[i]
        return -1 if dp[-1] == MAX else dp[-1]
