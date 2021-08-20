class Solution:

    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = float('inf')
        if n <= 4:
            return 0
        i = 3
        j = n - 1
        while i >= 0 and j >= 0:
            ans = min(ans, nums[j] - nums[i])
            i -= 1
            j -= 1
        return ans
