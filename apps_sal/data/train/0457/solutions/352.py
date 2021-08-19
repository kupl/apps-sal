class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        self.amount_dict = {0: 0}
        for coin in coins:
            self.amount_dict[coin] = 1
        return self.coinChangeHelp(amount)

    @lru_cache
    def coinChangeHelp(self, amount: int) -> int:
        if amount < 0:
            return -1
        if amount in self.amount_dict:
            return self.amount_dict[amount]
        max_coin = amount + 1
        for coin in self.coins:
            cur_coin = self.coinChangeHelp(amount - coin)
            if cur_coin >= 0:
                max_coin = min(max_coin, cur_coin + 1)
        max_coin = max_coin if max_coin != amount + 1 else -1
        self.amount_dict[amount] = max_coin
        return max_coin
