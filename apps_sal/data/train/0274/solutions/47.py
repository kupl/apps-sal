class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        small = []
        large = []
        res = 1
        left = 0
        for i in range(len(nums)):
            while small and nums[small[-1]] > nums[i]:
                small.pop()
            while large and nums[large[-1]] < nums[i]:
                large.pop()
            small.append(i)
            large.append(i)
            if small and large and (nums[large[0]] - nums[small[0]] > limit):
                left += 1
                if small[0] < left:
                    small.pop(0)
                if large[0] < left:
                    large.pop(0)
            res = max(res, i - left + 1)
        return res
