class Solution:
    def fonction(self, a, b, i, j, dp):
        if j == len(b) or i == len(a):
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if a[i] == b[j]:
            dp[i][j] = 1 + self.fonction(a, b, i + 1, j + 1, dp)
            return dp[i][j]
        dp[i][j] = max(self.fonction(a, b, i + 1, j + 1, dp), self.fonction(a, b, i, j + 1, dp), self.fonction(a, b, i + 1, j, dp))
        return dp[i][j]

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = []
        for i in range(len(A)):
            dp.append([-1] * len(B))
        return self.fonction(A, B, 0, 0, dp)
