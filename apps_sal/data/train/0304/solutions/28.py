class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:

        ages = sorted(ages, reverse=True)
        n = len(ages)

        dp = [0] * n
        res = 0

        for i in range(n):

            if i > 0 and ages[i] == ages[i - 1]:
                dp[i] = dp[i - 1]
                res += dp[i]
                continue

            for j in range(i + 1, n):
                if ages[j] <= 0.5 * ages[i] + 7:
                    break
                else:
                    dp[i] += 1

            res += dp[i]

        return res
