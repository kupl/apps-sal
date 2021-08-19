class Solution:

    def maxSatisfaction(self, s: List[int]) -> int:
        s.sort()
        l = len(s)
        dp = [[0 for _ in range(l)] for _ in range(l)]
        for i in range(l):
            for j in range(l):
                if j <= i:
                    if j == 0:
                        dp[i][j] = (j + 1) * s[i]
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + (j + 1) * s[i]
        print(max(dp[-1]))
        return max(max(dp[-1]), 0)
