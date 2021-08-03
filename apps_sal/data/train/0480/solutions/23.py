class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:

        self.steps = steps
        self.arrLen = arrLen
        self.memo = {}
        return self.dfs(steps, 0)

    def dfs(self, n, pos):
        if n == pos:
            return 1
        if n < pos or pos > self.arrLen - 1:
            return 0

        if (n, pos) in self.memo:
            return self.memo[(n, pos)]

        ans = 0

        if pos > 0:
            ans += self.dfs(n - 1, pos - 1)
        ans += self.dfs(n - 1, pos)

        if pos != self.arrLen - 1:
            ans += self.dfs(n - 1, pos + 1)

        ans %= 10**9 + 7
        self.memo[(n, pos)] = ans

        return ans
