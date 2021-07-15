class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        original = slices
        slices = slices[:-1]
        dp = [[0 for j in range(len(original) // 3 + 1)] for i in range(len(slices) + 1)]
        
        for j in range(1, len(original) // 3 + 1):
            dp[1][j] = slices[0]
        
        for j in range(1, len(dp[0])):
            for i in range(2, len(dp)):
                dp[i][j] = max(dp[i - 1][j], dp[i - 2][j - 1] + slices[i - 1], dp[i][j])
        ans = dp[-1][-1]
        slices = original[1:]

        dp = [[0 for j in range(len(original) // 3 + 1)] for i in range(len(slices) + 1)]
        
        for j in range(1, len(original) // 3 + 1):
            dp[1][j] = slices[0]
        
        for j in range(1, len(dp[0])):
            for i in range(2, len(dp)):
                dp[i][j] = max(dp[i - 1][j], dp[i - 2][j - 1] + slices[i - 1], dp[i][j])
        

        ans = max(ans, dp[-1][-1])
        return ans
            

