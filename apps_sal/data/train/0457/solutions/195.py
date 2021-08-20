class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [0] + [float('inf')] * amount
        for j in range(1, amount + 1):
            for i in range(n):
                if j >= coins[i]:
                    dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        return dp[-1] if dp[-1] < float('inf') else -1


"    \nclass Solution:\n    def coinChange(self, coins: List[int], amount: int) -> int:\n        @lru_cache(None)\n        def dp(remain, cnt):\n            if remain == 0:return cnt \n            ans = float('inf')\n            for c in coins:\n                if c*(ans-cnt)>remain>=c: \n                    ans = min(ans, dp(remain-c, cnt+1))\n            return ans \n        ans = dp(amount, 0) \n        return ans if ans < float('inf')  else -1\n    \n    \n    def coinChange(self, coins, amount):\n        coins.sort(reverse = True)\n        lenc, self.res = len(coins), 2**31-1\n\n        def dfs(pt, rem, count):\n            if not rem:\n                self.res = min(self.res, count)\n            for i in range(pt, lenc):\n                if coins[i] <= rem < coins[i] * (self.res-count): # if hope still exists\n                    dfs(i, rem-coins[i], count+1)\n\n        for i in range(lenc):\n            dfs(i, amount, 0)\n        return self.res if self.res < 2**31-1 else -1\n"
