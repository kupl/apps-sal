class Solution:

    def __init__(self):
        self.min_coins = float('inf')

    def coinChange(self, coins: List[int], amount: int) -> int:
        def getChange(num_coins, need, start):
            divided_coin = need // coins[start]

            if num_coins + divided_coin >= self.min_coins:
                return

            if need % coins[start] == 0:
                self.min_coins = min(self.min_coins, divided_coin + num_coins)
                return

            if start == len(coins) - 1:
                return

            for num_used in range(divided_coin, -1, -1):
                new_need = need - (coins[start] * num_used)
                getChange(num_coins + num_used, new_need, start + 1)

        coins = sorted(coins, reverse=True)
        getChange(0, amount, 0)

        return self.min_coins if self.min_coins < float('inf') else -1
