class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        coinValues = collections.defaultdict(list)
        for coin in coins:
            for i in range(coin, amount+1):
                if dp[i-coin] + 1 < dp[i]:
                    dp[i] = dp[i-coin] + 1
                    coinValues[i] = coinValues[i-coin] + [coin]
        print(coinValues[amount])
        return dp[-1] if dp[-1] != float('inf') else -1
