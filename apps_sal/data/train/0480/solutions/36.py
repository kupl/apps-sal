class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if arrLen == 1:
            return 1
        memo = {}
        return self.dfs(steps, arrLen, 0, memo)

    def dfs(self, steps, arrLen, currpos, memo):
        if (steps, currpos) in memo:
            return memo[(steps, currpos)]

        if currpos < 0 or currpos >= arrLen:
            return 0

        if steps == 0:
            if currpos == 0:
                return 1
            else:
                return 0

        memo[(steps, currpos)] = self.dfs(steps - 1, arrLen, currpos, memo) + self.dfs(steps - 1, arrLen, currpos + 1, memo) + self.dfs(steps - 1, arrLen, currpos - 1, memo)

        return memo[(steps, currpos)] % (10**9 + 7)
