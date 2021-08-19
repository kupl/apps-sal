class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount+1):
                if coin <= x:
                    dp[x] = min(dp[x], dp[x-coin]+1)

        return dp[amount] if dp[amount] != float('inf') else -1
        """
        '\n        def helper(amount):\n            if amount < 0:\n                return -1\n            elif amount == 0:\n                return 0\n            minCoins = None\n            for coin in coins:\n                totCoins = 1 + helper(amount - coin)\n                \n                if totCoins > 0 and (minCoins is None or totCoins < minCoins):\n                    minCoins = totCoins\n            if minCoins is None:\n                return -1\n            else:\n                return minCoins\n        return helper(amount)\n        '

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
