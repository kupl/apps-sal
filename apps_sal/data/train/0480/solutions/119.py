class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        memo = {(0, 0): 1}
        N = 10 ** 9 + 7

        def dfs(x, t):
            if (x, t) not in memo:
                if x < 0 or x >= arrLen:
                    res = 0
                elif x > t or x > steps - t:
                    res = 0
                else:
                    res = dfs(x + 1, t - 1) + dfs(x, t - 1) + dfs(x - 1, t - 1)
                memo[x, t] = res % N
            return memo[x, t]
        return dfs(0, steps)
