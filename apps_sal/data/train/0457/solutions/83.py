class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount+1):
                if coin <= x:
                    dp[x] = min(dp[x], dp[x-coin]+1)

        return dp[amount] if dp[amount] != float('inf') else -1
        '''
        '''
        def helper(amount):
            if amount < 0:
                return -1
            elif amount == 0:
                return 0
            minCoins = None
            for coin in coins:
                totCoins = 1 + helper(amount - coin)
                
                if totCoins > 0 and (minCoins is None or totCoins < minCoins):
                    minCoins = totCoins
            if minCoins is None:
                return -1
            else:
                return minCoins
        return helper(amount)
        '''
        def dfs(start, amt, n_coins):
            nonlocal min_coins

            coin = coins[start]

            div = amt // coin
            n_coins += div
            amt %= coin

            if amt == 0:
                min_coins = min(min_coins, n_coins)
                return

            if start < len_coins:
                dfs(start + 1, amt, n_coins)

                next_coin = coins[start + 1]

                for _ in range(div):
                    amt += coin
                    n_coins -= 1

                    if (min_coins - n_coins - 1) * next_coin + 1 > amt:
                        dfs(start + 1, amt, n_coins)
                    else:
                        break

        len_coins = len(coins) - 1

        coins.sort(reverse=True)

        min_coins = float('inf')

        dfs(0, amount, 0)

        return min_coins if min_coins < float('inf') else -1
