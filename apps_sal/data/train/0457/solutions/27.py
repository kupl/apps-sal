class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        if amount == 0:
            return 0
        elif amount < 0:
            return -1
        else:
            arr = []
            for i in coins:
                rv = self.coinChange(coins, amount - i)
                if rv != -1:
                    arr.append(rv)
            if not arr:
                return -1
            else:
                return min(arr) + 1
        '''
        dp = [amount + 1 for i in range(amount + 1)]
        dp[0] = 0
        for i in range(amount + 1):
            for c in coins:
                if c <= i and dp[i] > dp[i - c] + 1:
                    dp[i] = dp[i - c] + 1
        return -1 if dp[amount] > amount else dp[amount]
