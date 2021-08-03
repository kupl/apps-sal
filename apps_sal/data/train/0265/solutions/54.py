class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        # TC: O(N), SC:O(N)
        n = len(nums)
        # prefix sum
        for i in range(1, n):
            nums[i] += nums[i - 1]
        seen, dp = {0: -1}, [0] * n
        for i in range(n):
            x = nums[i] - target
            if x in seen:
                dp[i] = max(dp[i - 1], dp[seen[x]] + 1)
            else:
                dp[i] = dp[i - 1]
            seen[nums[i]] = i
        return dp[-1]
