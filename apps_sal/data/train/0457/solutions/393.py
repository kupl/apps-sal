class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = {}
        coins = sorted(coins)

#         q=deque()
#         q.append(amount)

#         while q:
#             node=q.popleft()
#             for coin in coins[::-1]:
#                 diff=node-coin
#                 if diff==0:
#                     return dp[node]+1
#                 elif diff>0:
#                     if diff not in dp:
#                         dp[diff]=1+dp[node]
#                         q.append(diff)

#         return -1

        dp = {coin: 1 for coin in coins}

        def helper(amount):
            if amount == 0:
                return 0

            if amount in dp:
                return dp[amount]

            dp[amount] = float('inf')
            for i in range(len(coins) - 1, -1, -1):
                if amount - coins[i] >= 0:
                    dp[amount] = min(dp[amount], 1 + helper(amount - coins[i]))

            return dp[amount]

        result = helper(amount)
        if result == float('inf'):
            return -1
        else:
            return result
