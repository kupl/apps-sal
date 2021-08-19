class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #         dp = [float('inf')] * (amount + 1)
        #         dp[0] = 0

        #         for coin in coins:
        #             for x in range(coin, amount + 1):
        #                 dp[x] = min(dp[x], dp[x - coin] + 1)
        #         return dp[amount] if dp[amount] != float('inf') else -1

        queue = deque([])
        seen = set()
        queue.append((0, 0))

        while queue:
            summ, num_coins = queue.popleft()
            if summ == amount:
                return num_coins

            for coin in coins:
                if summ + coin <= amount and summ + coin not in seen:
                    queue.append((summ + coin, num_coins + 1))
                    seen.add(summ + coin)

        return -1
