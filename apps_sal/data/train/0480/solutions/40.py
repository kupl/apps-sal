class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        if arrLen == 1:
            return 1
        memo = {}
        return self.dfs(steps, arrLen, 0, memo)

    def dfs(self, steps, arrLen, cur_pos, memo):
        if (steps, cur_pos) in memo:
            return memo[steps, cur_pos]
        if cur_pos < 0 or cur_pos >= arrLen:
            return 0
        if steps == 0:
            if cur_pos == 0:
                return 1
            else:
                return 0
        memo[steps, cur_pos] = self.dfs(steps - 1, arrLen, cur_pos, memo) + self.dfs(steps - 1, arrLen, cur_pos - 1, memo) + self.dfs(steps - 1, arrLen, cur_pos + 1, memo)
        return memo[steps, cur_pos] % (10 ** 9 + 7)
