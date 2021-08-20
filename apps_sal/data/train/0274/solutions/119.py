class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        currmax = currmin = nums[0]
        start = 0
        res = 1
        for i in range(1, len(nums)):
            currmax = max(currmax, nums[i])
            currmin = min(currmin, nums[i])
            print(currmax, currmin)
            if currmax - currmin <= limit:
                res = max(res, i - start + 1)
            else:
                if currmax == nums[start]:
                    currmax = max(nums[start + 1:i + 1])
                if currmin == nums[start]:
                    currmin = min(nums[start + 1:i + 1])
                start += 1
        return res
