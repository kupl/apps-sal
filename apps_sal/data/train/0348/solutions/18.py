class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp0 = [0 for i in range(n)]
        dp1 = [0 for i in range(n)]
        dp0[0] = nums[0]
        dp1[0] = nums[0]
        ans = nums[0]
        for i in range(1, n):
            dp0[i] = max(dp0[i-1]+nums[i], nums[i])
            dp1[i] = max(dp1[i-1]+nums[i], nums[i])
            if i > 1:
                dp1[i] = max(nums[i], dp1[i-1]+nums[i], nums[i]+dp0[i-2])
            ans = max(ans, dp0[i], dp1[i])
        return ans
            

