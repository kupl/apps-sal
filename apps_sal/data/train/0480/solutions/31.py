class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:

        cases = {}

        def dfs(steps, pos):
            if (steps, pos) in cases:
                return cases[(steps, pos)]
            if steps == 0:
                return 1 if pos == 0 else 0
            if pos >= arrLen or pos < 0:
                return 0
            subcount = dfs(steps - 1, pos + 1) + dfs(steps - 1, pos) + dfs(steps - 1, pos - 1)
            cases[(steps, pos)] = subcount
            return subcount % (10**9 + 7)

        return dfs(steps, 0)
