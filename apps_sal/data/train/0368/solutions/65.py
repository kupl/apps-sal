class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        dp = [[0 for j in range(n + 1)] for i in range(n + 1)]
        for j in range(1, n + 1):
            dp[1][j] = satisfaction[j - 1]
        ans = 0
        for i in range(2, n + 1):
            for j in range(i, n + 1):
                dp[i][j] = dp[i - 1][j - 1]+satisfaction[ j -1] * i
                
                ans = max(ans, dp[i][j])
        
        return ans
                
        

