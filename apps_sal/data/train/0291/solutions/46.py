class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        dp = [0, 0]
        ans = 0
        for i, num in enumerate(arr):
            dp[0], dp[1] = dp[num % 2] + num % 2, dp[(num - 1) % 2] + (num - 1) % 2
            ans += dp[0]
        return ans % (10**9 + 7)
