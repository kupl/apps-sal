class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        cols = len(text2)
        
        dp = [[0 for j in range(cols)] for i in range(rows)]
        if text1[rows-1] == text2[cols-1]:
            dp[rows-1][cols-1] = 1
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if i == rows - 1 and j == cols-1:
                    continue
                print1 = False
                # if i == 2:
                #     print1 = True
                if print1:
                    print(i, j)
                right = 0
                down = 0
                rightdown = 0
                if i < rows - 1:
                    down = dp[i+1][j]
                if j < cols - 1:
                    right = dp[i][j+1]
                if i < rows - 1 and j < cols - 1:
                    rightdown = dp[i+1][j+1]
                # print(text1[i])
                # print(text2[j])
                # print(down)
                # print(right)
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + rightdown
                else:
                    dp[i][j] = max(down, right)
        print(dp)
        return dp[0][0]
