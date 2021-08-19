class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        start = 0
        end = 1
        maxi = nums[0]
        mini = nums[0]
        max_l = 1
        while start <= end and end < len(nums):
            maxi = max(maxi, nums[end])
            mini = min(mini, nums[end])
            if maxi - mini <= limit:
                max_l = max(max_l, end - start + 1)
            else:
                if nums[start] == maxi:
                    maxi = max(nums[start + 1:end + 1])
                if nums[start] == mini:
                    mini = min(nums[start + 1:end + 1])
                start += 1
            end += 1
        return max_l
