class Solution:
    def coinChangeCopy(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        dp = [amount + 1] * (amount + 1)
        for i in range(amount + 1):
            if i in coins:
                dp[i] = 1
                continue
            candidates = [dp[i - coin] + 1 for coin in coins if i - coin > 0]
            if candidates:
                dp[i] = min(candidates)
        print(dp)
        return -1 if dp[amount] > amount else dp[amount]

    def coinChange(self, coins, amount):
        if not amount:
            return 0

        coin_nums = [amount + 1] * (amount + 1)
        coins_set = set(coins)

        for i in range(amount + 1):
            if i in coins_set:
                coin_nums[i] = 1
                continue
            candidates = [coin_nums[i - coin] + 1 for coin in coins if i - coin > 0]
            if candidates:
                coin_nums[i] = min(candidates)
        return coin_nums[amount] if coin_nums[amount] <= amount else -1
