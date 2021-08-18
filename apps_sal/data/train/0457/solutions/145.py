'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [0] + [float('inf')] * amount
        for j in range(1, amount+1):
            for i in range(n):
                if j >= coins[i]:
                    dp[j] = min(dp[j], dp[j-coins[i]]+1)
        return dp[-1] if dp[-1] < float('inf') else -1
'''


class Solution:
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dp(remain, cnt):
            if remain == 0:return cnt 
            ans = float('inf')
            for c in coins:
                if remain>=c: 
                    ans = min(ans, dp(remain-c, cnt+1))
            return ans 
        ans = dp(amount, 0) 
        return ans if ans < float('inf')  else -1
    '''

    def coinChange(self, coins, amount):
        coins.sort(reverse=True)
        lenc, self.res = len(coins), 2**31 - 1

        def dfs(pt, rem, count):
            if not rem:
                self.res = min(self.res, count)
            for i in range(pt, lenc):
                if coins[i] <= rem < coins[i] * (self.res - count):
                    dfs(i, rem - coins[i], count + 1)

        for i in range(lenc):
            dfs(i, amount, 0)
        return self.res if self.res < 2**31 - 1 else -1
