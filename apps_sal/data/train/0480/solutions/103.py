class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # From index 0, we can venture out at most steps//2 additional steps and still
        # gurantee we can come back. The length of the array that we can cover is
        # therefore the 0-th cell, plus the steps//2 additional cells = steps//2 + 1
        # (we ideally always need steps to be even because, from index 0, we can hit at most
        # step//2 cells, and to come back we need again step//2 moves. But if it is odd,
        # the extra step modulo 2 does us no good, we can make use of at most step//2 moves
        # to the right and step//2 moves back, unable to make use of the extra step)
        n = min(steps//2 + 1, arrLen)
        f = [None] * (steps + 1)
        f[0] = [0] * n
        f[0][0] = 1
        for t in range(1, steps + 1):
            f[t] = [0] * n
            for i in range(n):
                f[t][i] = f[t-1][i]
                if i + 1 < n:
                    f[t][i] += f[t-1][i+1]
                if i - 1 >= 0:
                    f[t][i] += f[t-1][i-1]
        return f[steps][0] % (10**9 + 7)

        memo = {}
        def f(i, c):
            if c == 0:
                return 1 if i == 0 else 0
            if (i, c) in memo:
                return memo[(i, c)]
            cnt = f(i, c - 1)
            if i + 1 < arrLen:
                cnt += f(i + 1, c - 1)
            if i - 1 >= 0:
                cnt += f(i - 1, c - 1)
            memo[(i, c)] = cnt
            return cnt
        
        return f(0, steps) % (10**9 + 7)

