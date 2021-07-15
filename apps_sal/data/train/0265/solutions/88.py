class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        prefix_sum = [0] * n    # prefix_sum[i] = sum of nums[0...i] inclusive
        lookup = {}             # lookup[sum] = rightmost index st prefix_sum[idx] == sum
        dp = [0] * n            # dp[i] = most non overlapping subarrays = target in nums[0...i]
                                # dp[i] = max(dp[i - 1], dp[j] + 1 (if j+1...i == target)) if i > 0
                                # dp[0] = 1 if nums[0] == target else 0
        dp[0] = 1 if nums[0] == target else 0
        prefix_sum[0] = nums[0]
        lookup[nums[0]] = 0
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
            check_for = prefix_sum[i] - target
            cmp_val = 0
            if check_for in lookup:
                cmp_val = dp[lookup[check_for]] + 1                
            elif check_for == 0:
                cmp_val = 1
            dp[i] = max(dp[i - 1], cmp_val)
            lookup[prefix_sum[i]] = i
            
        return dp[-1]
    
        # 0 0 0
        # prefix_sum    [0, 0]
        # lookup        {0:1}
        # dp            [1, ]

