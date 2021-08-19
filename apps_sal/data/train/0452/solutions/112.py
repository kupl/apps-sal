class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        dp = [[math.inf for i in range(n)] for j in range(d)]
        for i in range(n):
            if i == 0:
                dp[0][0] = jobDifficulty[i]
            else:
                dp[0][i] = max(dp[0][i - 1], jobDifficulty[i])
        for i in range(1, d):
            for j in range(i, n):
                for k in range(j):
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + max(jobDifficulty[k + 1:j + 1]))
        # print(dp)
        return dp[-1][-1]

#         def go(l, day):
#             if l >= n:
#                 return math.inf
#             if day == d:
#                 return max(jobDifficulty[l:])
#             ans = math.inf
#             for i in range(l, n):
#                 ans = min(ans, go(i+1, day+1) + max(jobDifficulty[l:i+1]))
#             return ans
#         return go(0, 1)
