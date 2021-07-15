class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount, path):
            if amount < 0:
                return float('inf')
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            ans = float('inf')
            for i in coins:
                r = dfs(amount-i, path+1)
                if r != float('inf'):
                    ans = min(ans, r+1)
            memo[amount] = ans
            return ans
        ret = dfs(amount, 0)
        return ret if ret != float('inf') else -1

