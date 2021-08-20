import heapq


class Solution:

    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        if len(nums) == 5:
            nums.sort()
            return min((b - a for (a, b) in zip(nums, nums[1:])))
        a = heapq.nsmallest(4, nums)
        b = heapq.nlargest(4, nums)
        arr = a + b
        arr.sort()
        return min(arr[4] - arr[0], arr[5] - arr[1], arr[6] - arr[2], arr[7] - arr[3])
