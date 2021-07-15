class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        neg = pos = 0
        ret = 0
        end = start = 0
        while end < len(nums):
            start = end
            while end < len(nums) and nums[end]:
                if nums[end] < 0:
                    neg += 1
                if nums[end] > 0:
                    pos += 1
                if neg % 2 == 0:
                    ret = max(ret, end - start + 1)
                    print(ret)
                end += 1
            while neg % 2:
                if nums[start] < 0:
                    neg -= 1
                    ret = max(ret, end - start - 1)
                start += 1
            neg = pos = 0
            while end < len(nums) and nums[end] == 0:
                end += 1
        return ret

