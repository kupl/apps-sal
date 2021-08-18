class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [0] * n

        dp[0] = arr[0] % 2

        for i in range(1, n):
            if arr[i] % 2 == 0:
                dp[i] = dp[i - 1]
            else:
                dp[i] = i - dp[i - 1] + arr[i] % 2

        return sum(dp) % (1000000000 + 7)
