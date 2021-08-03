class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        memo = {}
        mod = 10**9 + 7

        return self.dfs(steps, arrLen, 0, memo, mod)

    def dfs(self, steps, arrLen, pos, memo, mod):
        if (steps, pos) in memo:
            return memo[(steps, pos)]

        if steps == 0:
            if pos == 0:
                memo[(steps, pos)] = 1
                return 1
            return 0

        tmp = 0
        for d in (-1, 0, 1):
            nxt = pos + d
            if not (0 <= nxt < arrLen) or (nxt > steps):
                continue
            tmp += self.dfs(steps - 1, arrLen, nxt, memo, mod) % mod

        tmp %= mod

        memo[(steps, pos)] = tmp

        return tmp
