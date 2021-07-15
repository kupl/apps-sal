class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        dp = {}
        def in_dict(val):
            return val in dp.keys() and dp[val]
        if not amount:
            return 0
        if coins[0] > amount:
            return -1
        for coin in coins:
            dp[coin] = 1
        for i in range (coins[0], min(amount, coins[-1]) + 1):
            if i in dp.keys():
                continue
            available_coins = [coin for coin in coins if coin <= i]
            possible_min_coins = [1 + dp[i-coin] for coin in available_coins if in_dict(i-coin)]
            dp[i] = min(possible_min_coins) if possible_min_coins else 0
        for i in range(coins[-1]+1, amount+1):
            possible_min_coins = [1 + dp[i-coin] for coin in coins if in_dict(i-coin)]
            dp[i] = min(possible_min_coins) if possible_min_coins else 0
        return dp[amount] or -1
