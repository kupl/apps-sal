class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        currMax = nums[0]
        currMin = nums[0]
        maxSize = 1
        beg = 0
        end = 0
        while end < len(nums):
            currMax = max(currMax, nums[end])
            currMin = min(currMin, nums[end])
            if currMax - currMin > limit:
                beg += 1
                if currMax == nums[beg - 1]:
                    while currMax == nums[beg]:
                        beg += 1
                    currMax = max(nums[beg:end + 1])
                if currMin == nums[beg - 1]:
                    while currMin == nums[beg]:
                        beg += 1
                    currMin = min(nums[beg:end + 1])
            else:
                end += 1
            maxSize = max(maxSize, end - beg)
        return maxSize
