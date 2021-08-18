class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        dp = {}
        return self.rec(group, profit, dp, 0, G, P) % (10 ** 9 + 7)

    def rec(self, grp, profit, dp, i, mem_left, pr):
        if i >= len(grp):
            if pr <= 0:
                return 1
            return 0
        pr = max(pr, 0)
        if (i, mem_left, pr) in dp:
            return dp[i, mem_left, pr]

        dp[i, mem_left, pr] = self.rec(grp, profit, dp, i + 1, mem_left, pr) % (10**9 + 7)
        if grp[i] <= mem_left:
            dp[i, mem_left, pr] += self.rec(grp, profit, dp, i + 1, mem_left - grp[i], pr - profit[i]) % (10**9 + 7)
        return dp[i, mem_left, pr]
