class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [None for i in range(amount + 1)]
        
        dp[0] = 0
        
        for i in range(1, amount + 1):
            result = None
            for coin in coins:
                if i - coin >= 0:
                    tmp = dp[i - coin]
                    if tmp is not None and (result is None or tmp + 1 < result):
                        result = tmp + 1
            dp[i] = result
        
        if dp[-1] is None:
            return -1
        
        return dp[-1]
