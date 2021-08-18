class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0 for i in range(2)]for i in range(n)]
        if arr[0] & 1:
            dp[0] = [0, 1]
        else:
            dp[0] = [1, 0]
        for i in range(1, len(arr)):
            if arr[i] & 1:
                dp[i][1] = dp[i - 1][0] + 1
                dp[i][0] = dp[i - 1][1]
            else:
                dp[i][1] = dp[i - 1][1]
                dp[i][0] = dp[i - 1][0] + 1
        return sum(x[1] for x in dp) % (10**9 + 7)
