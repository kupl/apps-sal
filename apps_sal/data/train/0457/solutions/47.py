class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [float('inf') for _ in range(amount + 1)]
        memo[0] = 0
        for i in range(1, len(memo)):
            minv = float('inf')
            for coin in coins:
                if i - coin >= 0 and memo[i - coin] < minv:
                    minv = memo[i - coin]
            memo[i] = 1 + minv
        return memo[amount] if memo[amount] != float('inf') else -1
