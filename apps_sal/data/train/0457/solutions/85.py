class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        coins_set = set(coins)
        for i in range(amount + 1):
            if i in coins_set:
                dp[i] = 1
                continue
            candidates = [dp[i - c] + 1 for c in coins if i - c >= 0]
            if candidates:
                dp[i] = min(candidates)
        return dp[amount] if dp[amount] <= amount else -1
