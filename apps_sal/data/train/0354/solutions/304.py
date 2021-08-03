class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        numFaces = len(rollMax)
        dp = [[0 for i in range(numFaces + 1)] for j in range(n + 1)]
        dp[0][numFaces] = 1
        for i in range(numFaces):
            dp[1][i] = 1
        dp[1][numFaces] = numFaces
        for i in range(2, n + 1):
            for j in range(numFaces):
                for k in range(1, rollMax[j] + 1):
                    if i - k < 0:
                        break
                    dp[i][j] += dp[i - k][numFaces] - dp[i - k][j]
            dp[i][numFaces] = sum(dp[i])
        return dp[n][numFaces] % 1000000007
