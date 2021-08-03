class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [None for _ in range(amount + 1)]
        ret = self.helper(coins, amount, dp)
        return ret if ret != float('inf') else -1

    def helper(self, coins: List[int], amount: int, dp) -> int:
        if amount == 0:
            return 0
        if amount < coins[0]:
            return float('inf')

        ans = float('inf')
        for coin in coins:
            if amount >= coin:
                if amount == coin:
                    ans = 0
                else:
                    tmp = self.helper(coins, amount - coin, dp) if dp[amount - coin] == None else dp[amount - coin]
                    if dp[amount - coin] == None:
                        dp[amount - coin] = tmp

                    ans = min(ans, tmp)

        return ans + 1 if ans != -1 else -1
