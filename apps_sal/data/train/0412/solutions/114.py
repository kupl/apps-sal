class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10**9 + 7
        dp = [[0] * (target + 1) for i in range(d + 1)]

        dp[0][0] = 1
        for i in range(1, d + 1):
            nxt = [[0] * (target + 1) for i in range(d + 1)]
            for j in range(1, target + 1):
                nxt[i][j] = sum(dp[i - 1][j - x] for x in range(1, f + 1) if j >= x) % mod
            dp = nxt
        return dp[-1][-1]

        # mod = 10**9 + 7
        # @lru_cache(None)
        # def dfs(d, curr):
        #     if d == 0:
        #         return curr == 0
        #     if d < 0 or curr < 0:
        #         return 0
        #     return sum(dfs(d - 1, curr - x) for x in range(1, f + 1)) % mod
        # return dfs(d, target)
