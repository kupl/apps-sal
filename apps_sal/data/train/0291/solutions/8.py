class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(arr) + 1)]
        for (i, num) in enumerate(arr):
            if num % 2 == 0:
                dp[i + 1][0] = dp[i][0]
                dp[i + 1][1] = dp[i][1] + 1
            else:
                dp[i + 1][0] = dp[i][1] + 1
                dp[i + 1][1] = dp[i][0]
        return sum((dp[i][0] for i in range(len(dp)))) % (10 ** 9 + 7)
