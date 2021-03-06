class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        queue = [[0, 0]]
        visited = {0}
        step = 0
        for (node, step) in queue:
            for coin in coins:
                if node + coin in visited:
                    continue
                if node + coin == amount:
                    return step + 1
                if node + coin < amount:
                    queue.append([node + coin, step + 1])
                    visited.add(node + coin)
        return -1
        "dp = [0] + [float('inf')] * amount\n        \n        for c in coins:\n            for i in range(c, amount + 1):\n                dp[i] = min(dp[i], dp[i-c] + 1)\n        return dp[-1] if dp[-1] != float('inf') else -1"
