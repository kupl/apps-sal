class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        BASE = 10 ** 9 + 7
        memo = {(0, 0): 1}

        def dfs(num, tar):
            nonlocal BASE
            if (num, tar) in memo:
                return memo[num, tar]
            if num == 0 or tar == 0:
                return -1
            cnt = 0
            for i in range(1, f + 1):
                sub = dfs(num - 1, tar - i)
                if sub != -1:
                    cnt += sub
            memo[num, tar] = cnt % BASE
            return memo[num, tar]
        dfs(d, target)
        return memo[d, target]
