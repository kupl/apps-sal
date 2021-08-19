class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:

        #         def numWays(self, steps: int, arrLen: int) -> int:
        #             if steps == 0 or arrLen == 1:
        #                 return 1

        #             visited = {}
        #             return self.helper(0, steps, arrLen, visited) % (10 ** 9 + 7)

        #         def helper(self, pos, steps, n, visited):
        #             if (pos, steps) in visited:
        #                 return visited[(pos, steps)]
        #             if steps == 0:
        #                 if pos == 0:
        #                     return 1
        #                 else:
        #                     return 0
        #             if pos > steps:
        #                 return 0
        #             res = self.helper(pos, steps-1, n, visited)
        #             if 0<=pos+1<n:
        #                 res += self.helper(pos+1, steps-1, n, visited)
        #             if 0<=pos-1<n:
        #                 res += self.helper(pos-1, steps-1, n, visited)
        #             visited[(pos, steps)] = res
        #             return visited[(pos, steps)]

        #
        # Solution 1: DFS + dict for recording ----- 680 ms (28.33%) / 113.1 MB (7.87%)
        # ------------------------------------------------------------------------------------------
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
