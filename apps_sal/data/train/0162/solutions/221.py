class Solution:
    def longestCommonSubsequence(self, stringA: str, stringB: str) -> int:
        lengthA = len(stringA)
        lengthB = len(stringB)
        dp = [[ 0 for j in range(lengthB + 1)] for i in range(lengthA + 1)]
        for i in range(1, lengthA + 1):
            for j in range(1, lengthB + 1):
                if stringA[i - 1] == stringB[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[lengthA][lengthB]

