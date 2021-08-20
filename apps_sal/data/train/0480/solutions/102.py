class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        n = min(steps // 2 + 1, arrLen)
        f = [None] * (steps + 1)
        f[0] = [0] * n
        f[0][0] = 1
        for t in range(1, steps + 1):
            f[t] = [0] * n
            for i in range(n):
                f[t][i] = f[t - 1][i]
                if i + 1 < n:
                    f[t][i] += f[t - 1][i + 1]
                if i - 1 >= 0:
                    f[t][i] += f[t - 1][i - 1]
        return f[steps][0] % (10 ** 9 + 7)
        memo = {}

        def f(i, c):
            if c == 0:
                return 1 if i == 0 else 0
            if (i, c) in memo:
                return memo[i, c]
            cnt = f(i, c - 1)
            if i + 1 < arrLen:
                cnt += f(i + 1, c - 1)
            if i - 1 >= 0:
                cnt += f(i - 1, c - 1)
            memo[i, c] = cnt
            return cnt
        return f(0, steps) % (10 ** 9 + 7)
