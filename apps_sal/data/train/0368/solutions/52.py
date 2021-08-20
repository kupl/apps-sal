class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        dp = [-1000000009] * (n + 1)
        dp[0] = 0
        for i in range(n):
            for j in range(i, -1, -1):
                dp[j + 1] = max(dp[j + 1], satisfaction[i] * (j + 1) + dp[j])
        answer = -1000000009
        for i in range(n + 1):
            answer = max(dp[i], answer)
        return answer
