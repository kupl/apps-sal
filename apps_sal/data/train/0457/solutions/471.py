class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        def dfs(start, amount, n_coins):
            coin = coins[start]
            div = amount // coin
            n_coins += div
            amount %= coin
            if amount == 0:
                self.minimum = min(n_coins, self.minimum)
                return
            if start < length:
                dfs(start + 1, amount, n_coins)
                next_coin = coins[start + 1]
                for _ in range(div):
                    amount += coin
                    n_coins -= 1
                    if (self.minimum - n_coins - 1) * next_coin + 1 > amount:
                        dfs(start + 1, amount, n_coins)
                    else:
                        break
        coins.sort(reverse=True)
        self.minimum = float('inf')
        length = len(coins) - 1
        dfs(0, amount, 0)
        return self.minimum if self.minimum < float('inf') else -1
