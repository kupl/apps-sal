class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        dp = [0] * len(arr)
        def get_dp(i):
            if dp[i] == 0:
                dp[i] = 1
                j = i-1
                while j >= 0 and arr[i] > arr[j] and i-j <= d:
                    dp[i] = max(dp[i], 1+get_dp(j))
                    j -= 1
                j = i+1
                while j < len(arr) and arr[i] > arr[j] and j-i <= d:
                    dp[i] = max(dp[i], 1+get_dp(j))
                    j += 1
            return dp[i]
        max_count = 0
        for i in range(len(arr)):
            max_count = max(max_count, get_dp(i))
        return max_count
                    

