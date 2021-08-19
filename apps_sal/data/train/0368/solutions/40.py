class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        dp = [[0] * len(satisfaction) for i in range(len(satisfaction))]
        maxVal = 0
        for i in range(len(satisfaction)):
            count = 1
            tempM = 0
            for j in range(i, len(satisfaction)):
                dp[i][j] = satisfaction[j] * count
                tempM += dp[i][j]
                count += 1
            maxVal = max(maxVal, tempM)
        return maxVal
