class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        A = nums
        n = len(A)
        dp = [[0, 0] for i in range(n + 1)]

        max_len = 0
        for i in range(1, n + 1):
            if A[i - 1] > 0:
                dp[i][0] = dp[i - 1][0] + 1
                dp[i][1] = dp[i - 1][1] + 1 if dp[i - 1][1] != 0 else 0
            elif A[i - 1] < 0:
                dp[i][0] = dp[i - 1][1] + 1 if dp[i - 1][1] != 0 else 0
                dp[i][1] = dp[i - 1][0] + 1
            else:
                dp[i][0] = 0
                dp[i][1] = 0
            max_len = max(max_len, dp[i][0])
        # print(dp)

        return max_len
