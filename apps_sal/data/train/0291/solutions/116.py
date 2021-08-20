class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        dp = [0] * len(arr)
        dp[0] = arr[0] & 1
        for i in range(1, len(arr)):
            if arr[i] & 1:
                dp[i] = i - dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1]
        return sum(dp) % (10 ** 9 + 7)
