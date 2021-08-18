'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for c in coins:
            for j in range(c, amount+1):
                dp[j] = min(dp[j], dp[j-c]+1)
        return dp[-1] if dp[-1] < float('inf') else -1


        

'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [0] + [float('inf')] * amount
        for j in range(1, amount + 1):
            for i in range(n):
                if j >= coins[i]:
                    dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        return dp[-1] if dp[-1] < float('inf') else -1
