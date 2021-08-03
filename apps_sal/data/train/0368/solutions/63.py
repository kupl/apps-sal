class Solution:
    def maxSatisfaction(self, s: List[int]) -> int:
        s.sort()
        n = len(s)
        dp = [0] * (n + 2)

        for dish in range(n - 1, -1, -1):
            maxT = n + 1
            for time in range(1, maxT):
                if dish == n - 1:
                    dp[time] = time * s[dish]
                else:
                    include = time * s[dish] + dp[time + 1]
                    dp[time] = max(include, dp[time])
            maxT -= 1

        return max(0, dp[1])
