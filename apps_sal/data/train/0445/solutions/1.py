class Solution:

    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        i = 3
        j = n - 1
        if n <= 4:
            return 0
        ans = float('inf')
        while i >= 0 and j >= 0:
            ans = min(ans, abs(nums[i] - nums[j]))
            i -= 1
            j -= 1
        return ans
