class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        width,depth = len(text1),len(text2)
        dp = [[0 for _ in range(width)] for _ in range(depth)]
        for i in range(depth):
            for j in range(width):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                if i == 0:
                    up = 0
                else:
                    up = dp[i-1][j]
                if j == 0:
                    left = 0
                else:
                    left = dp[i][j - 1]
                if (text2[i] == text1[j]):
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(left,up)
        for d in dp:print(d)
        return dp[-1][-1]
