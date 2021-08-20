class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1
        N = len(jobDifficulty)
        dp = {}

        def f(i, n):
            if N - i == n:
                return sum(jobDifficulty[i:])
            if n == 1:
                return max(jobDifficulty[i:])
            if (i, n) in dp:
                return dp[i, n]
            res = None
            curr = 0
            for j in range(i, N - n + 1):
                curr = max(curr, jobDifficulty[j])
                if not res:
                    res = curr + f(j + 1, n - 1)
                else:
                    res = min(res, curr + f(j + 1, n - 1))
            dp[i, n] = res
            return res
        return f(0, d)
