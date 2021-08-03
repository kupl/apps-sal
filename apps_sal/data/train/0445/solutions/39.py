class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # 1. replace 3 of the elements < num
        # 2. replace 3 of the elements > num
        # Calculate the difference between min and max
        n = len(nums)
        if n < 5:
            return 0
        ans = float('inf')
        nums.sort()
        for i in range(4):
            ans = min(ans, nums[n - 4 + i] - nums[i])
        return ans
