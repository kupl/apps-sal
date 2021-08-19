class Solution:

    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')
        nums.sort()
        if n <= 4:
            return 0
        i = 3
        j = n - 1
        while i >= 0 and j >= 0:
            ans = min(ans, abs(nums[j] - nums[i]))
            i -= 1
            j -= 1
        return ans
