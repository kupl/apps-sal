class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        coins.sort()
        for i in range(1, amount+1):
            tmp = [float('inf')]
            for coin in coins:
                if i-coin < 0: 
                        break 
                tmp.append(dp[i-coin])
            dp[i] = min(tmp) + 1
            
        return dp[amount] if dp[amount] != float('inf') else -1
