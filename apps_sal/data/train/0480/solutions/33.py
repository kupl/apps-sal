class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        memo = collections.defaultdict(int)
        def dfs(index, curr):
            if curr == steps:
                if index == 0:
                    return 1
                else:
                    return 0
            key = (index, curr)
            if key in memo:
                return memo[key]
            res = 0
            if index > 0:
                res += dfs(index - 1, curr + 1)
            if index < arrLen - 1:
                res += dfs(index + 1, curr + 1)
            res += dfs(index, curr + 1)
            memo[key] = res
            return res
        
        return dfs(0, 0) % (10 ** 9 + 7)

